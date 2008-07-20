%define name	trilinos
%define version 8.0.7
%define release %mkrel 1

%define	libaztecoo_major	3.6
%define	libaztecoo_name		%mklibname aztecoo %{libaztecoo_major}
%define	develaztecoo_name	%mklibname aztecoo -d

%define	libepetra_major		3.6
%define	libepetra_name		%mklibname epetra %{libepetra_major}
%define	develepetra_name	%mklibname epetra -d

%define	libepetraext_major	3.6
%define	libepetraext_name	%mklibname epetraext %{libepetraext_major}
%define	develepetraext_name	%mklibname epetraext -d

%define	libifpack_major		3.2
%define	libifpack_name		%mklibname ifpack %{libifpack_major}
%define	develifpack_name	%mklibname ifpack -d

%define	libml_major		6.1
%define	libml_name		%mklibname ml %{libml_major}
%define	develml_name	%mklibname ml -d

%define	libnox_major	8.0
%define	libnox_name		%mklibname nox %{libnox_major}
%define	develnox_name	%mklibname nox -d

%define	libteuchos_major	1.4
%define	libteuchos_name		%mklibname teuchos %{libteuchos_major}
%define	develteuchos_name	%mklibname teuchos -d

%define	libtriutils_major	1.3
%define	libtriutils_name	%mklibname triutils %{libtriutils_major}
%define	develtriutils_name	%mklibname triutils -d

%if %{mdkversion} <= 1020
%define f77	g77
%else
%define f77	gfortran
%endif

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Parallel solver algorithms and libraries 
License:	LGPL
Group:		System/Libraries
URL:		http://trilinos.sandia.gov/
Source:		http://trilinos.sandia.gov/download/files/%name-%version.tar.gz
Patch1:		%{name}-8.0.5-libtool.patch
Patch2:		trilinos-8.0.7-gcc4.3.patch
Patch3:		trilinos-8.0.7-fix-includedir.patch
%if %{mdkversion} <= 1020
BuildRequires:	gcc-g77
%else
BuildRequires:	gcc-gfortran
%endif
BuildRequires:	automake
BuildRequires:	lapack-devel
BuildRequires:	mpich2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The Trilinos Project is an effort to develop parallel so
libraries within an object-oriented so
large-scale, complex multi-physics engineering and scientific applications. A
unique design feature of Trilinos is its focus on packages.

%package -n %{libaztecoo_name}
Summary:	Main library for aztecoo
Group:		System/Libraries

%description -n %{libaztecoo_name}
AztecOO provides an object-oriented interface the the well-known Aztec so
library. Furthermore, it allows flexible construction of matrix and vector
arguments via Epetra matrix and vector classes. Finally, AztecOO provide
additional functionality not found in Aztec and any future enhancements to the
Aztec package will be available only through the AztecOO interfaces. 

%package -n %{develaztecoo_name}
Summary:	Headers for developing programs that will use aztecoo
Group:		Development/Other
Requires:	%{libaztecoo_name} = %{version}-%{release}
Provides:	aztecoo-devel = %{version}-%{release}
Obsoletes:	%{mklibname aztecoo %{libaztecoo_major} -d}

%description -n %{develaztecoo_name}
This package contains the headers that programmers will need to develop
applications which will use aztecoo.

%package -n %{libepetra_name}
Summary:	Main library for epetra
Group:		System/Libraries

%description -n %{libepetra_name}
Epetra provides the fundamental construction routines and services function
that are required for serial and parallel linear algebra libraries. Epetra
provides the underlying foundation for all Trilinos so

%package -n %{develepetra_name}
Summary:	Headers for developing programs that will use epetra
Group:		Development/Other
Requires:	%{libepetra_name} = %{version}-%{release}
Provides:	epetra-devel = %{version}-%{release}
Obsoletes:	%{mklibname epetra %{libepetra_major} -d}

%description -n %{develepetra_name}
This package contains the headers that programmers will need to develop
applications which will use epetra.

%package -n %{libepetraext_name}
Summary:	Main library for epetraext
Group:		System/Libraries

%description -n %{libepetraext_name}
EpetraExt provides the fundamental construction routines and services function
that are required for serial and parallel linear algebra libraries. EpetraExt
provides the underlying foundation for all Trilinos so

%package -n %{develepetraext_name}
Summary:	Headers for developing programs that will use epetraext
Group:		Development/Other
Requires:	%{libepetraext_name} = %{version}-%{release}
Provides:	epetraext-devel = %{version}-%{release}
Obsoletes:	%{mklibname epetraext %{libepetraext_major} -d}

%description -n %{develepetraext_name}
This package contains the headers that programmers will need to develop
applications which will use epetraext.

%package -n %{libifpack_name}
Summary:	Main library for ifpack
Group:		System/Libraries

%description -n %{libifpack_name}
IFPACK provides a suite of object-oriented algebraic preconditioners for the
solution of preconditioned iterative solvers. IFPACK constructors expect an
Epetra_RowMatrix object for construction. IFPACK is part of the Trilinos Solver
Project and IFPACK object interact well with other Trilinos classes. In
particular, IFPACK can be used as a preconditioner for AztecOO.

%package -n %{develifpack_name}
Summary:	Headers for developing programs that will use ifpack
Group:		Development/Other
Requires:	%{libifpack_name} = %{version}-%{release}
Provides:	ifpack-devel = %{version}-%{release}
Obsoletes:	%{mklibname ifpack %{libifpack_major} -d}

%description -n %{develifpack_name}
This package contains the headers that programmers will need to develop
applications which will use ifpack.

%package -n %{libml_name}
Summary:	Main library for ml
Group:		System/Libraries

%description -n %{libml_name}
ML is Sandia's main multigrid preconditioning package. ML is designed to so
arising primarily from elliptic PDE discretizations.

%package -n %{develml_name}
Summary:	Headers for developing programs that will use ml
Group:		Development/Other
Requires:	%{libml_name} = %{version}-%{release}
Provides:	ml-devel = %{version}-%{release}
Obsoletes:	%{mklibname ml %{libml_major} -d}

%description -n %{develml_name}
This package contains the headers that programmers will need to develop
applications which will use ml.

%package -n %{libnox_name}
Summary:	Main library for nox
Group:		System/Libraries

%description -n %{libnox_name}
NOX is short for Nonlinear Object-Oriented Solutions, and its objective is to
enable the efficient solution of the equation: , where . NOX is designed to
work with any linear algebra package and to be easily customized. NOX is part
of Sandia's Trilinos project.

LOCA, distributed as part of NOX, is short for Library of Continuation
Algorithms, and its objective is to compute families of solutions to and their
bifurcations.

%package -n %{develnox_name}
Summary:	Headers for developing programs that will use nox
Group:		Development/Other
Requires:	%{libnox_name} = %{version}-%{release}
Provides:	nox-devel = %{version}-%{release}
Obsoletes:	%{mklibname nox %{libnox_major} -d}

%description -n %{develnox_name}
This package contains the headers that programmers will need to develop
applications which will use nox.

%if 0
%package -n teuchos
Summary:	The Trilinos Tools Library
Group:		System/Libraries

%description -n teuchos
Teuchos provides a suite of common tools for Trilinos for developers to use.
These tools include BLAS/LAPACK wrappers, smart pointers, parameter lists, XML
parsers, etc.
%endif

%package -n %{libteuchos_name}
Summary:	Main library for teuchos
Group:		System/Libraries

%description -n %{libteuchos_name}
Teuchos provides a suite of common tools for Trilinos for developers to use.
These tools include BLAS/LAPACK wrappers, smart pointers, parameter lists, XML
parsers, etc.

%package -n %{develteuchos_name}
Summary:	Headers for developing programs that will use teuchos
Group:		Development/Other
Requires:	%{libteuchos_name} = %{version}-%{release}
Provides:	teuchos-devel = %{version}-%{release}
Obsoletes:	%{mklibname teuchos %{libteuchos_major} -d}

%description -n %{develteuchos_name}
This package contains the headers that programmers will need to develop
applications which will use teuchos.

%package -n %{libtriutils_name}
Summary:	Main library for triutils
Group:		System/Libraries

%description -n %{libtriutils_name}
TriUtils a package of utilities for other Trilinos packages.

%package -n %{develtriutils_name}
Summary:	Headers for developing programs that will use triutils
Group:		Development/Other
Requires:	%{libtriutils_name} = %{version}-%{release}
Provides:	triutils-devel = %{version}-%{release}
Obsoletes:	%{mklibname triutils %{libtriutils_major} -d}

%description -n %{develtriutils_name}
This package contains the headers that programmers will need to develop
applications which will use triutils.

%prep
%setup -q
%patch1 -p 1 -b .libtool
%patch2 -p0
%patch3 -p0
chmod 644 packages/ml/COPYRIGHT

%build
autoreconf -i

%configure2_5x \
    --enable-mpi \
    --with-mpi-libs='-lmpich -lpmpich -lrt' \
    --disable-new_package \
    --disable-export-makefiles \
    --with-cxxflags="-DMPICH_IGNORE_CXX_SEEK" \
    F77=%{f77}
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}%{_datadir}/%{name}
rm -rf %{buildroot}%{_includedir}/Trilinos_version.h
chmod 644 %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libaztecoo_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libaztecoo_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post -n %{libepetra_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libepetra_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post -n %{libepetraext_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libepetraext_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post -n %{libifpack_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libifpack_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post -n %{libml_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libml_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post -n %{libnox_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libnox_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post -n %{libteuchos_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libteuchos_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post -n %{libtriutils_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libtriutils_name} -p /sbin/ldconfig
%endif

%files -n %{libaztecoo_name}
%defattr(-,root,root)
%{_libdir}/libaztecoo-%{libaztecoo_major}.so

%files -n %{develaztecoo_name}
%defattr(-,root,root)
%doc packages/aztecoo/README
%{_includedir}/az_*
%{_includedir}/AztecOO*
%{_includedir}/AZOO_iterate.h
%{_includedir}/AZOO_printf.h
%{_includedir}/Aztec2Petra.h
%{_libdir}/libaztecoo.a
%{_libdir}/libaztecoo.la
%{_libdir}/libaztecoo.so

%files -n %{libepetra_name}
%defattr(-,root,root)
%{_libdir}/libepetra-%{libepetra_major}.so

%files -n %{develepetra_name}
%defattr(-,root,root)
%{_includedir}/Epetra_*
%{_libdir}/libepetra.a
%{_libdir}/libepetra.la
%{_libdir}/libepetra.so

%files -n %{libepetraext_name}
%defattr(-,root,root)
%{_libdir}/libepetraext-%{libepetraext_major}.so

%files -n %{develepetraext_name}
%defattr(-,root,root)
%{_includedir}/EpetraExt_*
%{_libdir}/libepetraext.a
%{_libdir}/libepetraext.la
%{_libdir}/libepetraext.so

%files -n %{libifpack_name}
%defattr(-,root,root)
%{_libdir}/libifpack-%{libifpack_major}.so

%files -n %{develifpack_name}
%defattr(-,root,root)
%doc packages/ifpack/{ChangeLog-IFPACK,README-IFPACK}
%{_includedir}/Ifpack*
%{_includedir}/icrout_cholesky_mex.h
%{_includedir}/ifp_parameters.h
%{_libdir}/libifpack.a
%{_libdir}/libifpack.la
%{_libdir}/libifpack.so

%files -n %{libml_name}
%defattr(-,root,root)
%{_libdir}/libml-%{libml_major}.so

%files -n %{develml_name}
%defattr(-,root,root)
%doc packages/ml/{README-ML,COPYRIGHT,ChangeLog-ML}
%{_includedir}/ml_*
%{_includedir}/MLAPI*
%{_includedir}/mli_solver.h
%{_libdir}/libml.a
%{_libdir}/libml.la
%{_libdir}/libml.so

%files -n %{libnox_name}
%defattr(-,root,root)
%{_libdir}/libnox-%{libnox_major}.so
%{_libdir}/libloca-%{libnox_major}.so

%files -n %{develnox_name}
%defattr(-,root,root)
%doc packages/nox/{README,LICENSE}
%{_includedir}/NOX*
%{_includedir}/LOCA*
%{_libdir}/libnox.a
%{_libdir}/libnox.la
%{_libdir}/libnox.so
%{_libdir}/libloca.a
%{_libdir}/libloca.la
%{_libdir}/libloca.so

%files -n %{libteuchos_name}
%defattr(-,root,root)
%{_libdir}/libteuchos-%{libteuchos_major}.so

%files -n %{develteuchos_name}
%defattr(-,root,root)
%{_includedir}/Teuchos_*
%{_libdir}/libteuchos.a
%{_libdir}/libteuchos.la
%{_libdir}/libteuchos.so

%files -n %{libtriutils_name}
%defattr(-,root,root)
%{_libdir}/libtriutils-%{libtriutils_major}.so

%files -n %{develtriutils_name}
%defattr(-,root,root)
%{_includedir}/Trilinos_Util*
%{_includedir}/Triutils_*
%{_includedir}/iohb.h
%{_libdir}/libtriutils.a
%{_libdir}/libtriutils.la
%{_libdir}/libtriutils.so
