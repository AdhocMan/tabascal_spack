# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDonfig(PythonPackage):
    """Donfig"""

    homepage = "https://github.com/pytroll/donfig"
    pypi = "donfig/donfig-0.8.1.post1.tar.gz"

    license("MIT")

    version("0.8.1.post1", sha256="3bef3413a4c1c601b585e8d297256d0c1470ea012afa6e8461dc28bfb7c23f52")
    version("0.8.1.post0", sha256="3475689b8525313207b464738aaf2e8b9869385ea660322887a288437a1e9a3b")
    version("0.8.1", sha256="d1773b550e5f1e0930dee03565ce610d1c53a9f9af95fcc46f587cc70e9d39ff")
    version("0.8.0", sha256="c3759f9500acda430775666e2dae0146f25b1e37acf12c57e55344118a089c71")

    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-versioneer +toml", type="build")
