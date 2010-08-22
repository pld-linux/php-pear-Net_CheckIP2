%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	CheckIP2
%define		_status		beta
%define		_pearname	Net_CheckIP2
%define		subver	RC3
%define		rel		1
Summary:	%{_pearname} - A package to determine if an IP (v4) is valid
Summary(pl.UTF-8):	%{_pearname} - pakiet do określania poprawności adresu IP (v4)
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	0.%{subver}.%{rel}
License:	MIT License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	b200f6521c59e235a60dbb961ab9a060
URL:		http://pear.php.net/package/Net_CheckIP2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_CheckIP2 is a PHP5 port of the Net_CheckIP package. It's a drop-in
replacement.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Net_CheckIP2 to port PHP5 pakietu Net_CheckIP.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Net_CheckIP2/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/CheckIP2.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Net_CheckIP2
