# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySkyfield(PythonPackage):
    """Skyfield"""

    homepage = "https://github.com/skyfielders/python-skyfield"
    pypi = "skyfield/skyfield-1.49.tar.gz"

    license("MIT")

    version("1.49", sha256="20883027b2bbf4017dd916b64faaeb3713a8f88d7c8e353c15cd030ac63be92c")
    version("1.48", sha256="8b81f15b65e0b826341b17bf9e1446a0af94e49ed5983c04f123da49c1045fe1")
    version("1.47", sha256="3ac3e178c20547fa8e86adae4fdebcc8b4a744a184394268ce55338426bfe208")

    depends_on("py-setuptools", type="build")

    depends_on("py-astropy@5:", type=("build", "run"))
    depends_on("py-lxml", type=("build", "run"))
    depends_on("py-mock", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-jplephem", type=("build", "run"))
    depends_on("py-sgp4", type=("build", "run"))
