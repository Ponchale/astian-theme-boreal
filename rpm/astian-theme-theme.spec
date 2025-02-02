Name:       astian-theme-boreal
Summary:    Astian_OS Boreal UI theme
Version:    0.1.0
Release:    1
Group:      System/GUI/Other
License:    LGPLv2.1
BuildArch:  noarch
URL:        https://github.com/Ponchale/astian-theme-boreal
Source0:    %{name}-%{version}.tar.bz2
 
%description
This package contains boreal theme graphic and sounds files.

%prep
%setup -q -n %{name}-%{version}

%build
%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/themes/boreal/meegotouch/icons
mkdir -p %{buildroot}%{_datadir}/themes/boreal/fontawesome/icons
mkdir -p %{buildroot}%{_datadir}/sounds/boreal/stereo

cp icons/fontawesome/* %{buildroot}%{_datadir}/themes/boreal/fontawesome/icons
cp icons/meegotouch/* %{buildroot}%{_datadir}/themes/boreal/meegotouch/icons
cp index.theme %{buildroot}%{_datadir}/themes/boreal/

cp sounds/boreal/stereo/* %{buildroot}%{_datadir}/sounds/boreal/stereo

ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-terminal.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-l-terminal.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-settings.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-l-settings.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-screenshot.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-screenshot.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-browser.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-browser.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-calculator.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-calculator.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-calendar.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-calendar.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-camera.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-camera.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-clock.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-clock.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-email.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-email.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-gallery.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-gallery.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-music.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-mediaplayer.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-conversation.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-messaging.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-notes.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-notes.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-documents.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-office.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-contacts.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-people.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-dialer.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-phone.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-settings.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-settings.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-terminal.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-shell.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-packages.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-store.png
ln -sf /usr/share/themes/boreal/meegotouch/icons/icon-app-weather.png %{buildroot}/usr/share/themes/boreal/meegotouch/icons/icon-launcher-weather.png

%post

%files
%defattr(-,root,root,-)
%{_datadir}/themes/boreal
%{_datadir}/sounds/boreal
