%define _dname	%(echo %{name} | cut -d- -f1)
Summary:	Pack of themes for pekwm
Summary(pl):	Zestaw motywów dla pekwm
Name:		pekwm-themes2
Version:	1.0
Release:	1
License:	GPL
Group:		Themes
Source0:	%{name}.tar.bz2
# Source0-md5:	884085e39a8d1ba581a33fcc45581f47
Buildarch:	noarch
Requires:	pekwm
Obsoletes:	pekwm-themes-pack2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	%{_datadir}/%{_dname}/themes

%description
23 Ounces of Glass - Originall artwork: pixelhead, ported by: Tilman Sauerbeck <tilman@code-monkey.de>
Glacier - Orginall artwork: Glacier, ported by cnx <ciano@medgen.univr.it>
Lave -  Originall artwork: pixelhead, ported by Joshua Beard <josh@hewbert.com>
QNX-Orange - Joshua Beard <josh@hewbert.com>
Sedation - Originall artwork: pixelmoose, ported by Joshua Beard <josh@hewbert.com>
adept-t - Tomas Green  <green@green.homelinux.net>
Atlantique - Orginall blueCrux, ported by Xumerle Luciano
bb-nyz -  Werner Hartnagel <werner@halesoft.de>
blueCrux - madKOT <mad_kot@mail.ru>
bluish -  tompen <tompen@tompa.homelinux.net>
crux - tompen <tompen@tompa.homelinux.net>
iony-g - Tomas Green <green@green.homelinux.net>
KDE2 -  George J. De Bruin <SoundChaser@myrealbox.com>
shade-blank - Tomas Green <green@green.homelinux.net>
True - regret <trueregret@yahoo.se>

%description -l pl
23 Ounces of Glass - Orgina³ zrobiony przez: pixelhead, zaadaptowany przez \
Tilman Sauerbeck <tilman@code-monkey.de>
Glacier - Orgina³ zrobiony przez: Glacier, zaadaptowany przez cnx <ciano@medgen.univr.it>
Lave -  Orgina³ zrobiony przez: pixelhead, zaadaptowany przez Joshua Beard <josh@hewbert.com>
QNX-Orange - Joshua Beard <josh@hewbert.com>
Sedation - Orgina³ zrobiony przez: pixelmoose, zaadaptowany przez Joshua Beard <josh@hewbert.com>
adept-t - Tomas Green  <green@green.homelinux.net>
Atlantique - Orgina³ blueCrux, zaadaptowany przez Xumerle Luciano
bb-nyz -  Werner Hartnagel <werner@halesoft.de>
blueCrux - madKOT <mad_kot@mail.ru>
bluish -  tompen <tompen@tompa.homelinux.net>
crux - tompen <tompen@tompa.homelinux.net>
iony-g - Tomas Green <green@green.homelinux.net>
KDE2 -  George J. De Bruin <SoundChaser@myrealbox.com>
shade-blank - Tomas Green <green@green.homelinux.net>
True - regret <trueregret@yahoo.se>

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themesdir}

cp -R * $RPM_BUILD_ROOT%{_themesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_themesdir}/*
