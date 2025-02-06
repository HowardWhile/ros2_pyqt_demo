from setuptools import find_packages, setup

import os
import glob
import subprocess

package_name = 'ros2_pyqt_demo'

# -----------------------------------------------------
# 自動轉換 .ui
# -----------------------------------------------------
def convert_ui():
    ui_files = glob.glob("ros2_pyqt_demo/*.ui")  
    output_dir = "ros2_pyqt_demo"
    os.makedirs(output_dir, exist_ok=True)
    for ui_file in ui_files:
        py_file = os.path.join(output_dir, f"ui_{os.path.basename(ui_file).replace('.ui', '.py')}")
        subprocess.run(["pyside6-uic", "-o", py_file, ui_file], check=True)
# -----------------------------------------------------
convert_ui()
# -----------------------------------------------------

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
