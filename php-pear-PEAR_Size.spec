# TODO
# - make it actually work with pld pear packaging (lots of file not found errors)
%define		subver		RC1
%define		rel			1
%define		status		beta
%define		pearname	PEAR_Size
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - determine and list how much filespace each installed package consumes
Summary(pl.UTF-8):	%{pearname} - narzędzie do określania miejsca zajmowanego przez zainstalowane klasy PEAR
Name:		php-pear-%{pearname}
Version:	1.0.0
Release:	0.%{subver}.%{rel}
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}%{subver}.tgz
# Source0-md5:	c9abddb4a283ba856524b05c0a48c454
URL:		http://pear.php.net/package/PEAR_Size/
BuildRequires:	php-pear-PEAR >= 1:1.4.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Console_Getargs >= 1.3.4
Requires:	php-pear-Console_Table >= 1.1.0
Requires:	php-pear-HTML_Table >= 1.8.2
Requires:	php-pear-PEAR >= 1:1.4.0
Obsoletes:	php-pear-PEAR_Size-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A commandline tool modeled on 'df' that lists how much filespace each
installed package consumes. A subset of packages can be specified as
can channels.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Wzorowane na `df' narzędzie do określania ile przestrzeni dyskowej
zajmuje zainstlowany pakiet. Zestaw pakietów może być określony w
postaci kanałów.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup
mv docs/PEAR_Size/docs/script-usage.txt .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install
install -p usr/bin/pearsize $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log script-usage.txt
%{php_pear_dir}/.registry/*.reg
%attr(755,root,root) %{_bindir}/pearsize
%{php_pear_dir}/PEAR/Command/Size.php
%{php_pear_dir}/PEAR/Command/Size.xml
%{php_pear_dir}/PEAR/Size
%{php_pear_dir}/PEAR/Size.php
