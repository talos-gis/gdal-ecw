# This setup.py file is licensed under MIT license.
# Other files on this project are licensed under a different license (see LICENSE.txt for details)

from setuptools import setup

package_name = 'gdal-ecw'
v = (3, 6, 4)
url = 'https://github.com/talos-gis/gdal-ecw'
maintainer = 'Idan Miara'
maintainer_email = 'idan@miara.com'

version = '.'.join(str(v) for v in v)
# a gdal plugin version A.B.C is compatible with gdal version A.B.D for any D.
install_requires = [f'gdal>={v[0]}.{v[1]},<{v[0]}.{v[1]+1}']
readme = open('../README.md', encoding="utf-8").read()
readme_type = 'text/markdown'

setup(
    name=package_name,
    version=version,
    url=url,
    maintainer=maintainer,
    maintainer_email=maintainer_email,
    packages=['osgeo', 'osgeo.gdalplugins', 'osgeo.data.gdal'],
    install_requires=install_requires,
    long_description=readme,
    long_description_content_type=readme_type,
    package_data={"": ["*.dll", "*.wkt"]},
)
