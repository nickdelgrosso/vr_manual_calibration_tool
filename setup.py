from setuptools import setup, find_packages

setup(name="vr_manual_calibration_tool",
      version="0.0.1",
      description="A projection alignment tool made for simple virtual reality CAVE setups, made at the Straw Lab's 2017 VR Bootcamp.",
      long_description=open("README.md").read(),
      classifiers=[ # Get strings from 
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering'
      ],
      keywords="virtual reality, projection mapping", # Separate with spaces
      author="Nicholas A. Del Grosso and Levente L. Orban",
      author_email="delgrosso.nick@gmail.com",
      license="Creative Commons",
      packages=find_packages(exclude=['examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      # TODO: List of packages that this one depends upon:   
      install_requires=['numpy', 'ratcave'],
      # TODO: List executable scripts, provided by the package (this is just an example)
      entry_points={
        'console_scripts': 
            ['projector_calibrate=projector_calibration:main']
      }
)