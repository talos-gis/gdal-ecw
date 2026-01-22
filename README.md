# gdal-ecw
GDAL ecw plugin as a python wheel for easy installation.
* DLL and LICENSE files were copied from [gisinternals](https://www.gisinternals.com/release.php)
* SDK version: MSVC 2022	x64	release-1930-x64-gdal-3-11-3-mapserver-8-4-0	2025-07-13 17:51:49
* SDK version: MSVC 2022	win32	release-1930-gdal-3-11-3-mapserver-8-4-0	2025-07-13 17:13:27

# Version compatibility
* `gdal-ecw==x.y.patch` is compatible with any `gdal>=x.y,<x.(y+1)`, 
meaning `gdal-ecw==3.6.4` is compatible with `gdal==3.6.x` for any `x`.
* `gdal-ecw` is tested against Christoph Gohlke's binary wheels
  * GDAL>=3.5 - https://github.com/cgohlke/gdal.whl/releases
  * GDAL<3.5 - https://www.lfd.uci.edu/~gohlke/pythonlibs/

# Troubleshooting:
* I get an error message: `ERROR 1: Can't load requested DLL: ..\site-packages\osgeo\gdalplugins\gdal_ECW_JP2ECW.dll
127: The specified procedure could not be found.`
  * You might not have Microsoft Visual C++ 2019 Redistributable - 
Download and install vc_redist.x86.exe or vc_redist.x64.exe from 
https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170
* No error message is given but the format is still unsupported after installation
  * In some gdal binary distribution versions `gdalplugins` directory is not set up by default:
    * Either set `GDAL_DRIVER_PATH` environment variable to the `gdalplugins` directory or 
    * uncomment the section in `osgeo/__init__.py`
