# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyJplephem(PythonPackage):
    """This package can load and use a Jet Propulsion Laboratory (JPL)
    ephemeris for predicting the position and velocity of a planet or other
    Solar System body."""

    pypi = "jplephem/jplephem-2.9.tar.gz"

    license("MIT")

    version("2.22", sha256="0d9acc7217b4806feba93e72974ceead5611104bce6789af38d4f27dcf7a592c")
    version("2.21", sha256="34194b610695f21b89217b9852b8dabadbce80848cb369d9567ef12dc4828d55")
    version("2.20", sha256="bb986d508ea46c68936a899689a644db5fa0af39c9a504422089a003eca0e1fa")
    version("2.19", sha256="c162454c656d6e5203ff9701d826671faf9f3209d971cbb68ddb46003dff6dcf")
    version("2.9", sha256="9dffb9f3d3f6d996ade875102431fe385e8ea422da25c8ba17b0508d9ca1282b")

    # pip silently replaces distutils with setuptools
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
