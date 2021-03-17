#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sys-Statistics-Linux
Version  : 0.66
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/B/BL/BLOONIX/Sys-Statistics-Linux-0.66.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BL/BLOONIX/Sys-Statistics-Linux-0.66.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libsys-statistics-linux-perl/libsys-statistics-linux-perl_0.66-2.debian.tar.xz
Summary  : 'Front-end module to collect system statistics'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Sys-Statistics-Linux-license = %{version}-%{release}
Requires: perl-Sys-Statistics-Linux-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(UNIVERSAL::require)

%description
NAME
Sys::Statistics::Linux - Front-end module to collect system statistics
SYNOPSIS
use Sys::Statistics::Linux;

%package dev
Summary: dev components for the perl-Sys-Statistics-Linux package.
Group: Development
Provides: perl-Sys-Statistics-Linux-devel = %{version}-%{release}
Requires: perl-Sys-Statistics-Linux = %{version}-%{release}

%description dev
dev components for the perl-Sys-Statistics-Linux package.


%package license
Summary: license components for the perl-Sys-Statistics-Linux package.
Group: Default

%description license
license components for the perl-Sys-Statistics-Linux package.


%package perl
Summary: perl components for the perl-Sys-Statistics-Linux package.
Group: Default
Requires: perl-Sys-Statistics-Linux = %{version}-%{release}

%description perl
perl components for the perl-Sys-Statistics-Linux package.


%prep
%setup -q -n Sys-Statistics-Linux-0.66
cd %{_builddir}
tar xf %{_sourcedir}/libsys-statistics-linux-perl_0.66-2.debian.tar.xz
cd %{_builddir}/Sys-Statistics-Linux-0.66
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Sys-Statistics-Linux-0.66/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Sys-Statistics-Linux
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Sys-Statistics-Linux/df23397441718ee5f6a8c88281b54f1806c799bd
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Sys::Statistics::Linux.3
/usr/share/man/man3/Sys::Statistics::Linux::Compilation.3
/usr/share/man/man3/Sys::Statistics::Linux::CpuStats.3
/usr/share/man/man3/Sys::Statistics::Linux::DiskStats.3
/usr/share/man/man3/Sys::Statistics::Linux::DiskUsage.3
/usr/share/man/man3/Sys::Statistics::Linux::FileStats.3
/usr/share/man/man3/Sys::Statistics::Linux::LoadAVG.3
/usr/share/man/man3/Sys::Statistics::Linux::MemStats.3
/usr/share/man/man3/Sys::Statistics::Linux::NetStats.3
/usr/share/man/man3/Sys::Statistics::Linux::PgSwStats.3
/usr/share/man/man3/Sys::Statistics::Linux::ProcStats.3
/usr/share/man/man3/Sys::Statistics::Linux::Processes.3
/usr/share/man/man3/Sys::Statistics::Linux::SockStats.3
/usr/share/man/man3/Sys::Statistics::Linux::SysInfo.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Sys-Statistics-Linux/df23397441718ee5f6a8c88281b54f1806c799bd

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Sys/Statistics/Linux.pm
/usr/lib/perl5/vendor_perl/5.32.1/Sys/Statistics/Linux/Compilation.pm
/usr/lib/perl5/vendor_perl/5.32.1/Sys/Statistics/Linux/CpuStats.pm
/usr/lib/perl5/vendor_perl/5.32.1/Sys/Statistics/Linux/DiskStats.pm
/usr/lib/perl5/vendor_perl/5.32.1/Sys/Statistics/Linux/DiskUsage.pm
/usr/lib/perl5/vendor_perl/5.32.1/Sys/Statistics/Linux/FileStats.pm
/usr/lib/perl5/vendor_perl/5.32.1/Sys/Statistics/Linux/LoadAVG.pm
/usr/lib/perl5/vendor_perl/5.32.1/Sys/Statistics/Linux/MemStats.pm
/usr/lib/perl5/vendor_perl/5.32.1/Sys/Statistics/Linux/NetStats.pm
/usr/lib/perl5/vendor_perl/5.32.1/Sys/Statistics/Linux/PgSwStats.pm
/usr/lib/perl5/vendor_perl/5.32.1/Sys/Statistics/Linux/ProcStats.pm
/usr/lib/perl5/vendor_perl/5.32.1/Sys/Statistics/Linux/Processes.pm
/usr/lib/perl5/vendor_perl/5.32.1/Sys/Statistics/Linux/SockStats.pm
/usr/lib/perl5/vendor_perl/5.32.1/Sys/Statistics/Linux/SysInfo.pm
