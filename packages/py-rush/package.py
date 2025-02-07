# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRush(PythonPackage):
    """Rush"""

    homepage = "https://github.com/sigmavirus24/rush"
    pypi = "rush/rush-2021.4.0.tar.gz"

    license("MIT")

    version("2021.4.0", sha256="818624075f0313f64a4c38ba62bc4a6526ee31b463990c8aebf03a98f5aaf264")

    depends_on("py-setuptools", type="build")
