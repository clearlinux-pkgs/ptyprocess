#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ptyprocess
Version  : 0.5.1
Release  : 10
URL      : https://pypi.python.org/packages/source/p/ptyprocess/ptyprocess-0.5.1.tar.gz
Source0  : https://pypi.python.org/packages/source/p/ptyprocess/ptyprocess-0.5.1.tar.gz
Summary  : Run a subprocess in a pseudo terminal
Group    : Development/Tools
License  : ISC
Requires: ptyprocess-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Launch a subprocess in a pseudo terminal (pty), and interact with both the
process and its pty.

%package python
Summary: python components for the ptyprocess package.
Group: Default

%description python
python components for the ptyprocess package.


%prep
%setup -q -n ptyprocess-0.5.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489025281
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489025281
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
