# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLogbook(PythonPackage):
    """Logbook"""

    homepage = "https://github.com/getlogbook/logbook"
    pypi = "logbook/logbook-1.8.0.tar.gz"

    license("MIT")

    version("1.8.0", sha256="487fa41539787bfa21a51fabd7f3ae8ae7f9e6679bb3e241d0f5f18a2fc37e9c")

    depends_on("py-setuptools", type="build")
    depends_on("py-cython", type="build")

    #  depends_on("python@:3.10", type=("build", "run"))
