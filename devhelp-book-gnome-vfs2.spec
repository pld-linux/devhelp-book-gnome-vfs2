Summary:	DevHelp book: gnome-vfs
Summary(pl):	Ksi±¿ka do DevHelp'a o gnome-vfs
Name:		devhelp-book-gnome-vfs
Version:	2.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gnome-vfs-2.0.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about gnome-vfs 1.2

%description -l pl
Ksi±¿ka do DevHelp o gnome-vfs 1.2

%prep
%setup -q -c gnome-vfs-%{version} -n gnome-vfs-%{version}

%build
mv -f book gnome-vfs-%{version}
mv -f book.devhelp gnome-vfs-%{version}.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/gnome-vfs
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install gnome-vfs-%{version}.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install gnome-vfs-%{version}/* $RPM_BUILD_ROOT%{_prefix}/books/gnome-vfs

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
