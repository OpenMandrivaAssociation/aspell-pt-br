%define language_code pt_BR
%define upstream_name aspell6-%{language_code}
%define upstream_version 20090702-0

Name:		aspell-pt-br
Version: 	20131030_12_0
Release: 	%mkrel 1

Summary: 	The Brazilian Portuguese dictionary for Aspell.
License: 	GPL
Group: 		System/Internationalization
URL: 		http://aspell.net/
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/pt_BR/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
make
dicdir=`aspell dump config dict-dir`

######################################################################
%install
rm -rf %{buildroot}
make install

mkdir -p %{buildroot}%{_docdir}/%{name}
cp README %{buildroot}%{_docdir}/%{name}
cp COPYING %{buildroot}%{_docdir}/%{name}
pushd doc
cp NEWS %{buildroot}%{_docdir}/%{name}
cp LEIAME_*.txt %{buildroot}%{_docdir}/%{name}
cp README_*.txt %{buildroot}%{_docdir}/%{name}
popd


######################################################################
%clean
rm -fr %{buildroot}


######################################################################
%files
%defattr(-,root,root)
%{_docdir}/%{name}/
%(aspell dump config dict-dir)/

