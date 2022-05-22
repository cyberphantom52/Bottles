# runtime.py
#
# Copyright 2020 brombinmirko <send@mirko.pm>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from pathlib import Path
from functools import lru_cache

from bottles.backend.globals import Paths  # pyright: reportMissingImports=false


class RuntimeManager:

    @staticmethod
    @lru_cache
    def get_runtimes(_filter: str = "bottles"):
        runtimes = {
            "bottles": RuntimeManager.__get_bottles_runtime(),
            "steam": RuntimeManager.__get_steam_runtime()
        }

        if _filter == "steam":
            if len(runtimes.get("steam", {})) == 0:
                return False

        return runtimes.get(_filter, False)

    @staticmethod
    def get_runtime_env(_filter: str = "bottles"):
        runtime = RuntimeManager.get_runtimes(_filter)

        if runtime:
            env = ':'.join(runtime)
        else:
            return False

        ld = os.environ.get('LD_LIBRARY_PATH')
        if ld:
            env += f":{ld}"

        return env

    @staticmethod
    def __get_runtime(paths: list, structure: list):
        def check_structure(found, expected):
            for e in expected:
                if e not in found:
                    return False
            return True

        for runtime_path in paths:
            if not os.path.exists(runtime_path):
                continue

            structure_found = []
            for root, dirs, files in os.walk(runtime_path):
                for d in dirs:
                    structure_found.append(d)

            if not check_structure(structure_found, structure):
                continue

            res = [f"{runtime_path}/{s}" for s in structure]

            return res

        return False

    @staticmethod
    def __get_bottles_runtime():
        paths = [
            "/app/etc/runtime",
            Paths.runtimes
        ]
        structure = ["lib", "lib32"]

        return RuntimeManager.__get_runtime(paths, structure)

    @staticmethod
    def __get_steam_runtime():
        from bottles.backend.managers.steam import SteamManager
        available_runtimes = {}
        steam_path = SteamManager.find_steam_path()

        if not steam_path:
            return available_runtimes

        lookup = {
            "soldier": {
                "name": "soldier",
                "entry_point": os.path.join(steam_path, "steamapps/common/SteamLinuxRuntime_soldier/_v2-entry-point"),
            },
            "scout": {
                "name": "scout",
                "entry_point": os.path.join(steam_path, "ubuntu12_32/steam-runtime/run.sh"),
            }
        }

        for name, data in lookup.items():
            if not os.path.exists(data["entry_point"]):
                continue

            available_runtimes[name] = data

        return available_runtimes
