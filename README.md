[![](http://github-actions.40ants.com/AndrewSazonov/test_pycrysfml08_build/matrix.svg)](https://github.com/AndrewSazonov/test_pycrysfml08_build/actions)

This is a repository for testing the build process of both the fortran crystallographic library [CrysFML2008](https://code.ill.fr/rodriguez-carvajal/CrysFML2008) and its python interface [PyCrysFML08](https://code.ill.fr/scientific-software/PyCrysFML08).

Main steps:
* Clone the [CrysFML2008](https://code.ill.fr/rodriguez-carvajal/CrysFML2008) project.
* Build the CrysFML2008 lybrary with the `gfortran` or `ifort` fortran compiler using the [CMake](https://cmake.org/) or [FPM](https://fpm.fortran-lang.org/) build system.
* Clone the [PyCrysFML08](https://code.ill.fr/scientific-software/PyCrysFML08) project.
* Build selected PyCrysFML08 modules with `gfortran` or `ifort`
* Run tests with `pytest`.

More details are in the [CI script](.github/workflows/main.yml).
