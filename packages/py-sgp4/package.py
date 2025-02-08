# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySgp4(PythonPackage):
    """Track earth satellite TLE orbits using up-to-date 2010 version of SGP4"""

    homepage = "https://github.com/brandon-rhodes/python-sgp4"
    pypi = "sgp4/sgp4-1.4.tar.gz"

    license("MIT")

    version("2.23", sha256="d8addc53a2fb9f88dee6bfd401d2865b014cc0b57bf2cee69bdee8d9685d5429")
    version("2.22", sha256="17f0a2eaad2dca065b6de25c1ceaa940ff7cfa8cc67120cb4111a00f177b86f9")
    version("2.21", sha256="6179b875044877e941633c20af7722fd231a88d8a89af01bf30bd64f33cdecef")
    version("2.20", sha256="9fde328872f484eb644dabe32122ba617570ff61b548b7200a9d63629ac3097c")
    version("2.19", sha256="ffad58b31bf1316829fa432f6f63fbdff80c1b2d9012926ae4e1f294a8772087")
    version("1.4", sha256="1fb3cdbc11981a9ff34a032169f83c1f4a2877d1b6c295aed044e1d890b73892")

    depends_on("python@2.6:2.8,3.3:", type=("build", "run"))
    # pip silently replaces distutils with setuptools
    depends_on("py-setuptools", type="build")
