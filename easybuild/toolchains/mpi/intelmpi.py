##
# Copyright 2012 Stijn De Weirdt
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
Support for Intel MPI as toolchain MPI library.
"""

from easybuild.tools.toolchain.mpi import Mpi


TC_CONSTANT_INTELMPI = "IntelMPI"


class IntelMPI(Mpi):
    """Intel MPI class"""
    MPI_MODULE_NAME = ['impi']
    MPI_FAMILY = TC_CONSTANT_INTELMPI

    MPI_LIBRARY_NAME = 'mpi'

    ## echo "   1. Command line option:  -cc=<compiler_name>"
    ## echo "   2. Environment variable: I_MPI_CC (current value '$I_MPI_CC')"
    ## echo "   3. Environment variable: MPICH_CC (current value '$MPICH_CC')"
    ## cxx -> cxx only
    ## intel mpicc only support few compiler names (and eg -cc='icc -m32' won't work.)

    # FIXME: does this need to be here? if so, why?
    MPI_UNIQUE_OPTION_MAP = {
                             '_opt_MPICF90':'-fc="%(F90_base)s"',
                             }

    # turns out MPICC="mpicc -cc='icc' " isn't always working, e.g. with configure
    MPI_COMPILER_MPICC = 'mpiicc'
    MPI_COMPILER_MPICXX = 'mpiicpc'

    MPI_COMPILER_MPIF77 = 'mpiifort'
    MPI_COMPILER_MPIF90 = 'mpiifort'

    MPI_SHARED_OPTION_MAP = {
                             '_opt_MPICC': '', #cc="%(CC_base)s"',
                             '_opt_MPICXX':'', #cxx="%(CXX_base)s"',
                             '_opt_MPIF77':'', #fc="%(F77_base)s"',
                             '_opt_MPIF90':'', #f90="%(F90_base)s"',
                             }
