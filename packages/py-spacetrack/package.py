# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySpacetrack(PythonPackage):
    """Spacetrack"""

    homepage = "https://github.com/python-astrodynamics/spacetrack"
    pypi = "spacetrack/spacetrack-1.3.1.tar.gz"

    license("MIT")

    version("1.3.1", sha256="9d26fca0948b7affae5767148c333d13c97eef33a25dcd1a49312f4fe51b87af")
    version("1.3.0", sha256="0d2d80b929c3253c71e98839d882d7af1ca7272fc89eda5e293448096766f8ba")
    version("1.2.0", sha256="e4ee633f4d86461dc0683771609826e8df26448ceb98193960676c74e3eda14f")

    depends_on("py-setuptools", type="build")
    depends_on("py-versioneer +toml", type="build")

    # test with python 3.11 first
    #  depends_on("python@:3.10", type=("build", "run"))
    depends_on("py-httpx", type=("build", "run"))
    depends_on("py-logbook@0.12.3:", type=("build", "run"))
    depends_on("py-python-dateutil", type=("build", "run"))
    depends_on("py-represent@1.4.0:", type=("build", "run"))
    depends_on("py-rush", type=("build", "run"))
    depends_on("py-sniffio", type=("build", "run"))
    depends_on("py-attrs", type=("build", "run"))
