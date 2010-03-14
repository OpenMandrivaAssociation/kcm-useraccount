%define kde_version     4.4.1

Summary: 	Webcam support for KDE users
Name: 		kcm-useraccount
Version: 	0.2.1
Release: 	%mkrel 2
Source:		119405-kcm.tar.gz
License: 	GPLv2+
Group: 		Graphical desktop/KDE
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: 		http://kde-apps.org/content/show.php?content=119405
BuildRequires:  kdelibs4-devel
BuildRequires:  kdebase4-devel
BuildRequires:	opencv-devel
Provides:	kdepasswd
%description
This is a modified version of Password & User Account section in System Settings, add webcam support for user image. 
This modification is based on Opencv library basically because it is multiplatform.

%files
%defattr(-,root,root)
%doc README  
%{_kde_libdir}/kde4/*.so
%{_kde_services}/*
##%{_kde_datadir}/locale/*/*/kio_gopher.mo
%{_kde_datadir}/apps/kdm/pics/users/Blackbox.png
%{_kde_datadir}/apps/kdm/pics/users/Green.png
%{_kde_datadir}/apps/kdm/pics/users/Happy.png
%{_kde_datadir}/apps/kdm/pics/users/Listening.png
%{_kde_datadir}/apps/kdm/pics/users/Notme.png
%{_kde_datadir}/apps/kdm/pics/users/TV.png
%{_kde_datadir}/apps/kdm/pics/users/bomb.png
%{_kde_datadir}/config.kcfg/kcm_useraccount.kcfg
%{_kde_datadir}/config.kcfg/kcm_useraccount_pass.kcfg


#--------------------------------------------------------------------

%prep
%setup -qn kcm

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT


