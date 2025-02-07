# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyKatversion(PythonPackage):
    """katversion"""

    homepage = "https://github.com/ska-sa/katversion"
    pypi = "katversion/katversion-1.2.tar.gz"

    license("BSD")

    version("1.2", sha256="87c5d49a9a448fdef4de8ab03b8ae83552d2f7577d8d7402ec2a0a7edd6964a2")
    version("1.1", sha256="9571a6bdb246284a4ae840e6e455b49b2b36db74a6e23b9ee1a51e32eb77c8c7")
    version("1.0", sha256="b8923bad16de756d6eb26850ecc69e2f336b1f58485d764c1e2e40efca106c6d")

    depends_on("py-setuptools", type="build")
