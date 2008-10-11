%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	Size
%define		_status		alpha
%define		_pearname	PEAR_Size
Summary:	%{_pearname} - determine and list how much filespace each installed package consumes
Summary(pl.UTF-8):	%{_pearname} - narzędzie do określania miejsca zajmowanego przez zainstalowane klasy PEAR
Name:		php-pear-%{_pearname}
Version:	0.1.8
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	22b8d7d67e041d919525fb75db4569ec
URL:		http://pear.php.net/package/PEAR_Size/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Console_Getargs >= 1.3.4
Requires:	php-pear-Console_Table >= 1.1.0
Requires:	php-pear-HTML_Table >= 1.8.2
Requires:	php-pear-PEAR >= 1:1.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A commandline tool modeled on 'df' that lists how much filespace each
installed package consumes. A subset of packages can be specified as
can channels.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Wzorowane na `df' narzędzie do określania ile przestrzeni dyskowej
zajmuje zainstlowany pakiet. Zestaw pakietów może być określony w
postaci kanałów.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install
install usr/bin/pearsize $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/PEAR_Size/{docs/script-usage.txt,TODO}
%{php_pear_dir}/.registry/*.reg
%attr(755,root,root) %{_bindir}/pearsize
%{php_pear_dir}/PEAR/Command/*
%{php_pear_dir}/PEAR/Size
%{php_pear_dir}/PEAR/Size.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/%{_pearname}
