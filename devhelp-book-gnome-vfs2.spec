Summary:	DevHelp book: gnome-vfs 2.0
Summary(pl):	Ksi±¿ka do DevHelpa o gnome-vfs 2.0
Name:		devhelp-book-gnome-vfs2
Version:	2.0
Release:	1
License:	GPL
Group:		X11/Applications
#Source0:	http://www.devhelp.net/books/books/gnome-vfs-2.0.tar.gz
Source0:	gnome-vfs-2.0.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about gnome-vfs 2.0.

%description -l pl
Ksi±¿ka do DevHelpa o gnome-vfs 2.0.

%prep
%setup -q -c -n gnome-vfs-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/gnome-vfs-2.0,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/gnome-vfs-%{version}.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/gnome-vfs-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
