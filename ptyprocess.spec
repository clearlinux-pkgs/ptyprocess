#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ptyprocess
Version  : 0.6.0
Release  : 30
URL      : https://pypi.debian.net/ptyprocess/ptyprocess-0.6.0.tar.gz
Source0  : https://pypi.debian.net/ptyprocess/ptyprocess-0.6.0.tar.gz
Summary  : Run a subprocess in a pseudo terminal
Group    : Development/Tools
License  : ISC
Requires: ptyprocess-python3
Requires: ptyprocess-license
Requires: ptyprocess-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

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
Requires: ptyprocess-python3

%description python
python components for the ptyprocess package.


%package python3
Summary: python3 components for the ptyprocess package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ptyprocess package.


%prep
%setup -q -n ptyprocess-0.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530278910
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/ptyprocess
cp LICENSE %{buildroot}/usr/share/doc/ptyprocess/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/ptyprocess/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
