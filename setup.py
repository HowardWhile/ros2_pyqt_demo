from setuptools import find_packages, setup
import glob

package_name = 'ros2_pyqt_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('lib/' + package_name, glob.glob("ros2_pyqt_demo/ui_*.py")),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Howard',
    maintainer_email='makubex49@gmail.com',
    description='my demo',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'demo = ros2_pyqt_demo.mainwindow:main'
        ],
    },
)
