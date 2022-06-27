class Samples:
    data = {
        "notifications": []
    }

    config = {
        "Name": "",
        "Arch": "win64",
        "Windows": "win10",
        "Runner": "",
        "WorkingDir": "",
        "DXVK": "",
        "NVAPI": "",
        "VKD3D": "",
        "LatencyFleX": "",
        "Path": "",
        "Custom_Path": False,
        "Environment": "",
        "Creation_Date": "",
        "Update_Date": "",
        "Versioning": False,
        "State": 0,
        "Parameters": {
            "dxvk": False,
            "dxvk_hud": False,
            "dxvk_nvapi": False,
            "vkd3d": False,
            "latencyflex": False,
            "mangohud": False,
            "obsvkc": False,
            "vkbasalt": False,
            "gamemode": False,
            "gamescope": False,
            "gamescope_game_width": 0,
            "gamescope_game_height": 0,
            "gamescope_window_width": 0,
            "gamescope_window_height": 0,
            "gamescope_fps": 0,
            "gamescope_fps_no_focus": 0,
            "gamescope_scaling": False,
            "gamescope_borderless": False,
            "gamescope_fullscreen": True,
            "sync": "wine",
            "fsr": False,
            "fsr_level": 5,
            "custom_dpi": 96,
            "renderer": "gl",
            "discrete_gpu": False,
            "virtual_desktop": False,
            "virtual_desktop_res": "1280x720",
            "pulseaudio_latency": False,
            "fullscreen_capture": False,
            "take_focus": False,
            "mouse_warp": True,
            "fixme_logs": False,
            "use_runtime": False,
            "use_eac_runtime": True,
            "use_be_runtime": True,
            "use_steam_runtime": False,
        },
        "Environment_Variables": {},
        "Installed_Dependencies": [],
        "DLL_Overrides": {},
        "External_Programs": {},
        "Uninstallers": {},
        "Latest_Executables": [],
        "Language": "sys"
    }

    environments = {
        "gaming": {
            "Runner": "wine",
            "Parameters": {
                "dxvk": True,
                # "nvapi": True,
                "vkd3d": False,
                "sync": "esync",
                "fsr": False,
                "discrete_gpu": True,
                "pulseaudio_latency": True
            },
            "Installed_Dependencies": [
                "d3dx9",
                "msls31",
                "arial32",
                "times32",
                "courie32",
                "d3dcompiler_43",
                "d3dcompiler_47"
            ]
        },
        "application": {
            "Runner": "wine",
            "Parameters": {
                "dxvk": True,
                "vkd3d": True
            },
            "Installed_Dependencies": [
                "arial32",
                "times32",
                "courie32",
                # "mono",
                # "dotnet40",
                # "dotnet48"
            ]
        },
        "layered": {
            "Runner": "wine",
            "Layers": {}
        },
    }

    bottles_to_steam_relations = {
        "DXVK_HUD": ("dxvk_hud", True),
        "MANGOHUD": ("mangohud", True),
        "OBS_VKCAPTURE": ("obsvkc", True),
        "ENABLE_VKBASALT": ("vkbasalt", True),
        "WINEESYNC": ("sync", "esync"),
        "WINEFSYNC": ("sync", "fsync"),
        "WINEFSYNC_FUTEX2": ("sync", "futex2"),
        "WINE_FULLSCREEN_FSR": ("fsr", True),
        "WINE_FULLSCREEN_FSR_STRENGTH": ("fsr_level", None),
        "DRI_PRIME": ("discrete_gpu", True),
        "__NV_PRIME_RENDER_OFFLOAD": ("discrete_gpu", True),
        "PULSE_LATENCY_MSEC": ("pulseaudio_latency", True),
        "PROTON_EAC_RUNTIME": ("use_eac_runtime", True),
        "PROTON_BATTLEYE_RUNTIME": ("use_be_runtime", True)
    }
