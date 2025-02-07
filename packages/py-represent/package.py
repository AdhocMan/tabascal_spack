# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRepresent(PythonPackage):
    """Represent"""

    homepage = "https://github.com/RazerM/represent"
    pypi = "Represent/Represent-2.1.tar.gz"

    license("MIT")

    version("2.1", sha256="0b2d015c14e7ba6b3b5e6a7ba131a952013fe944339ac538764ce728a75dbcac")
    version("2.0", sha256="352ec74c11e49959867ad3ceedb029376d815b199bf588458c1298815378012b")
    version("1.6.0.post0", sha256="026c0de2ee8385d1255b9c2426cd4f03fe9177ac94c09979bc601946c8493aa0")
    version("1.6.0", sha256="293dfec8b2e9e2150a21a49bfec2cd009ecb600c8c04f9186d2ad222c3cef78a")
    version("1.5.1", sha256="9c12c1c60b8616f97855d3a37ea4ec60e3d5d463965a6a29b80d0b794ad4f0d8")

    depends_on("py-setuptools", type="build")
