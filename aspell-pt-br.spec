%define language_code pt_BR
%define upstream_name aspell6-%{language_code}
%define upstream_version %(echo %{version} |sed -e 's,_,-,g')

Name:		aspell-pt-br
Version: 	20131030_12_0
Release: 	1
Summary: 	The Brazilian Portuguese dictionary for Aspell.
License: 	GPL
Group: 		System/Internationalization
URL: 		http://aspell.net/
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/pt_BR/%{upstream_name}-%{upstream_version}.tar.bz2
BuildArch:	noarch
Requires:      aspell >= 0.60

%description
This package contains the Brazilian Portuguese (pt_BR) dictionary for
Aspell, adding support for that language to the GNU Aspell checker.


######################################################################
%prep
%setup -q -n %{upstream_name}-%{upstream_version}


######################################################################
%build
sh ./configure --vars DESTDIR=%{buildroot}
%make_build
dicdir=`aspell dump config dict-dir`

######################################################################
%install
%make_install

######################################################################
%files
%defattr(-,root,root)
%doc README
%(aspell dump config dict-dir)/

