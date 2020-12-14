#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ptyprocess
Version  : 0.6.0
Release  : 39
URL      : https://pypi.debian.net/ptyprocess/ptyprocess-0.6.0.tar.gz
Source0  : https://pypi.debian.net/ptyprocess/ptyprocess-0.6.0.tar.gz
Summary  : Run a subprocess in a pseudo terminal
Group    : Development/Tools
License  : ISC
Requires: ptyprocess-license = %{version}-%{release}
Requires: ptyprocess-python = %{version}-%{release}
Requires: ptyprocess-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Launch a subprocess in a pseudo terminal (pty), and interact with both the
process and its pty.

%package license
Summary: license components for the ptyprocess package.
Group: Default

%description license
license components for the ptyprocess package.


%package python
Summary: python components for the ptyprocess package.
Group: Default
Requires: ptyprocess-python3 = %{version}-%{release}

%description python
python components for the ptyprocess package.


%package python3
Summary: python3 components for the ptyprocess package.
Group: Default
Requires: python3-core
Provides: pypi(ptyprocess)

%description python3
python3 components for the ptyprocess package.


%prep
%setup -q -n ptyprocess-0.6.0
cd %{_builddir}/ptyprocess-0.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603399513
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ptyprocess
cp %{_builddir}/ptyprocess-0.6.0/LICENSE %{buildroot}/usr/share/package-licenses/ptyprocess/db1f866b29c6a191752c7c5924b7572cdbc47c34
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ptyprocess/db1f866b29c6a191752c7c5924b7572cdbc47c34

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
