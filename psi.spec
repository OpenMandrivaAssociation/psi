%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Jabber client using Qt4
Name:		psi
Version:	1.3
Release:	1
License:	GPLv2+
Group:		Networking/Instant messaging
Url:		http://psi-im.org
Source0:	http://prdownloads.sourceforge.net/psi/%{name}-%{version}.tar.xz
Source1:	%{name}-icons.tar.bz2
Source2:	%{name}-smileysets.tar.bz2
Source3:	%{name}-iconsets.tar.bz2
BuildRequires:	cmake ninja
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(qca2-qt5)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Positioning)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5WebChannel)
BuildRequires:	cmake(Qt5WebEngineCore)
BuildRequires:	cmake(Qt5WebEngine)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(libidn)
Requires:	%{name}-lang-pack = %{EVRD}
Requires:	%{_lib}qca2-plugin-openssl
Suggests:	%{_lib}qca2-plugin-gnupg
#Suggests:	psi-plugin-media

#Translations files has been moved on psi website, you can update them using this little script
#For the main psi translation
#for i in be cs de eo es es_ES fr it ja mk pl pt_BR ru sl sv uk ur_PK vi zh_CN zh_TW ;do wget http://psi-im.org/download/lang/psi_${i}.qm && bzip2 -f psi_${i}.qm;done 

%define langlist be cs de eo es es_ES fr it ja mk pl pt_BR ru sl sv uk ur_PK vi zh_CN zh_TW
%{expand:%(\
	i=4; \
	for lang in %langlist; do\
		echo "%%{expand:Source$i: %%{name}_$lang.qm.bz2}";\
		i=$[i+1];\
	done\
	)
}
%{expand:%(for lang in %{langlist}; do echo "%%{expand:%%define build_$lang 1}"; done)}

%description
Psi is the premiere Instant Messaging application designed for Microsoft
Windows, Apple Mac OS X and GNU/Linux. Built upon an open protocol named
Jabber, Psi is a fast and lightweight messaging client that utilises the best
in open source technologies.
The goal of the Psi project is to create a powerful, yet easy-to-use
Jabber/XMPP client that tries to strictly adhere to the XMPP drafts.and Jabber
JEPs. This means that in most cases, Psi will not implement a feature unless
there is an accepted standard for it in the Jabber community. Doing so ensures
that Psi will be compatible, stable, and predictable, both from an end-user and
developer standpoint.

%files
%doc README COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/client_icons.txt
%dir %{_datadir}/%{name}/certs
%{_datadir}/%{name}/certs/README
%{_datadir}/%{name}/certs/startcom_ca.crt
%{_datadir}/%{name}/certs/startcom_ca_new.crt
%dir %{_datadir}/%{name}/iconsets
%dir %{_datadir}/%{name}/iconsets/emoticons
%{_datadir}/%{name}/iconsets/emoticons/default/
%dir %{_datadir}/%{name}/iconsets/roster
%{_datadir}/%{name}/iconsets/roster/README
%{_datadir}/%{name}/iconsets/roster/*.jisp
%{_datadir}/%{name}/iconsets/roster/default/
%dir %{_datadir}/%{name}/iconsets/system
%{_datadir}/%{name}/iconsets/system/README
%{_datadir}/%{name}/iconsets/system/default/
%{_datadir}/%{name}/iconsets/activities
%{_datadir}/%{name}/iconsets/affiliations
%{_datadir}/%{name}/iconsets/clients
%{_datadir}/%{name}/iconsets/moods
%{_datadir}/%{name}/themes
%{_datadir}/%{name}/sound/

#--------------------------------------------------------------------

%package -n %{name}-iconsets
Summary:	Package with iconsets
Group:		Networking/Instant messaging
Requires:	%{name} = %{EVRD}

%description -n %{name}-iconsets
This package contain a various iconsets for psi.

%files -n %{name}-iconsets
%{_datadir}/%{name}/iconsets/system/amibulb.jisp
%{_datadir}/%{name}/iconsets/system/amiglobe.jisp
%{_datadir}/%{name}/iconsets/system/berlin-icq.jisp
%{_datadir}/%{name}/iconsets/system/berlin.jisp
%{_datadir}/%{name}/iconsets/system/chrome.jisp
%{_datadir}/%{name}/iconsets/system/dudes.jisp
%{_datadir}/%{name}/iconsets/system/dudes2.jisp
%{_datadir}/%{name}/iconsets/system/email.jisp
%{_datadir}/%{name}/iconsets/system/gothRoster.jisp
%{_datadir}/%{name}/iconsets/system/individual.jisp
%{_datadir}/%{name}/iconsets/system/kitty.jisp
%{_datadir}/%{name}/iconsets/system/lightbulb.jisp
%{_datadir}/%{name}/iconsets/system/msn6.jisp
%{_datadir}/%{name}/iconsets/system/neos.jisp
%{_datadir}/%{name}/iconsets/system/speechbubbles.jisp
%{_datadir}/%{name}/iconsets/system/stellar.jisp

#--------------------------------------------------------------------

%package -n %{name}-smileysets
Summary:	Package with smileysets
Group:		Networking/Instant messaging
Requires:	%{name} = %{EVRD}

%description -n %{name}-smileysets
This package contain a various smileysets for psi.

%files -n %{name}-smileysets
%{_datadir}/%{name}/iconsets/emoticons/AIM.jisp
%{_datadir}/%{name}/iconsets/emoticons/Chibi.jisp
%{_datadir}/%{name}/iconsets/emoticons/JIM.jisp
%{_datadir}/%{name}/iconsets/emoticons/KMess-Cartoon-1.0.jisp
%{_datadir}/%{name}/iconsets/emoticons/Ninja.jisp
%{_datadir}/%{name}/iconsets/emoticons/Taryn.jisp
%{_datadir}/%{name}/iconsets/emoticons/apple_ichat-1.0.jisp
%{_datadir}/%{name}/iconsets/emoticons/critters-1.0.jisp
%{_datadir}/%{name}/iconsets/emoticons/gadu-gadu.jisp
%{_datadir}/%{name}/iconsets/emoticons/icq-2002a.jisp
%{_datadir}/%{name}/iconsets/emoticons/ikonboard-3.1.jisp
%{_datadir}/%{name}/iconsets/emoticons/invision_board-1.0.1.jisp
%{_datadir}/%{name}/iconsets/emoticons/kreativ_squareheads.jisp
%{_datadir}/%{name}/iconsets/emoticons/megapack-1.0.jisp
%{_datadir}/%{name}/iconsets/emoticons/msn.jisp
%{_datadir}/%{name}/iconsets/emoticons/patricks_faces-1.0.jisp
%{_datadir}/%{name}/iconsets/emoticons/shinyicons.jisp
%{_datadir}/%{name}/iconsets/emoticons/tlen.pl-3.73.jisp
%{_datadir}/%{name}/iconsets/emoticons/trill-basic-smileys.jisp
%{_datadir}/%{name}/iconsets/emoticons/webmessenger.jisp
%{_datadir}/%{name}/iconsets/emoticons/wpkontakt-2.4.1.jisp
%{_datadir}/%{name}/iconsets/emoticons/yahoo_messenger.jisp

#--------------------------------------------------------------------

%package -n %{name}-lang-pack-en
Summary:	English language pack for psi
Group:		System/Internationalization
Requires:	locales-en
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-en
This package adds support for english to psi.

%files -n %{name}-lang-pack-en

#--------------------------------------------------------------------

%if %{build_be}
%package -n %{name}-lang-pack-be
Summary:	Belarusian language pack for psi
Group:		System/Internationalization
Requires:	locales-be
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-be
This package adds support for belarusian to psi.

%files -n %{name}-lang-pack-be
%{_datadir}/%{name}/%{name}_be.qm
%endif

#--------------------------------------------------------------------

%if %{build_cs}
%package -n %{name}-lang-pack-cs
Summary:	Czech language pack for psi
Group:		System/Internationalization
Requires:	locales-cs
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-cs
This package adds support for czech to psi.

%files -n %{name}-lang-pack-cs
%{_datadir}/%{name}/%{name}_cs.qm
%endif

#--------------------------------------------------------------------

%if %{build_de}
%package -n %{name}-lang-pack-de
Summary:	Deutsch language pack for psi
Group:		System/Internationalization
Requires:	locales-de
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-de
This package adds support for deutsch to psi.

%files -n %{name}-lang-pack-de
%{_datadir}/%{name}/%{name}_de.qm
%endif

#--------------------------------------------------------------------

%if %{build_eo}
%package -n %{name}-lang-pack-eo
Summary:	Esperanto language pack for psi
Group:		System/Internationalization
Requires:	locales-eo
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-eo
This package adds support for esperanto to psi.

%files -n %{name}-lang-pack-eo
%{_datadir}/%{name}/%{name}_eo.qm
%endif

#--------------------------------------------------------------------

%if %{build_es}
%package -n %{name}-lang-pack-es
Summary:	Spanish language pack for psi
Group:		System/Internationalization
Requires:	locales-es
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-es
This package adds support for spanish to psi.

%files -n %{name}-lang-pack-es
%{_datadir}/%{name}/%{name}_es.qm
%{_datadir}/%{name}/%{name}_es_ES.qm
%endif
#--------------------------------------------------------------------

%if %{build_fr}
%package -n %{name}-lang-pack-fr
Summary:	French language pack for psi
Group:		System/Internationalization
Requires:	locales-fr
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-fr
This package adds support for french to psi.

%files -n %{name}-lang-pack-fr
%{_datadir}/%{name}/%{name}_fr.qm
%endif

#--------------------------------------------------------------------

%if %{build_it}
%package -n %{name}-lang-pack-it
Summary:	Italian language pack for psi
Group:		System/Internationalization
Requires:	locales-it
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-it
This package adds support for italian to psi.

%files -n %{name}-lang-pack-it
%{_datadir}/%{name}/%{name}_it.qm
%endif

#--------------------------------------------------------------------

%if %{build_ja}
%package -n %{name}-lang-pack-ja
Summary:	Japanese language pack for psi
Group:		System/Internationalization
Requires:	locales-ja
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-ja
This package adds support for japanese to psi.

%files -n %{name}-lang-pack-ja
%{_datadir}/%{name}/%{name}_ja.qm
%endif

#--------------------------------------------------------------------

%if %{build_mk}

%package -n %{name}-lang-pack-mk
Summary:	Macedonia language pack for psi
Group:		System/Internationalization
Requires:	locales-mk
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-mk
This package adds support for macedonia to psi.

%files -n %{name}-lang-pack-mk
%{_datadir}/%{name}/%{name}_mk.qm
%endif

#--------------------------------------------------------------------

%if %{build_pl}
%package -n %{name}-lang-pack-pl
Summary:	Polish language pack for psi
Group:		System/Internationalization
Requires:	locales-pl
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-pl
This package adds support for polish to psi.

%files -n %{name}-lang-pack-pl
%{_datadir}/%{name}/%{name}_pl.qm
%endif

#--------------------------------------------------------------------

%if %{build_pt_BR}
%package -n %{name}-lang-pack-pt_br
Summary:	Portuguese brazilian language pack for psi
Group:		System/Internationalization
Requires:	locales-pt
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-pt_br
This package adds support for portuguese brazilian to psi.

%files -n %{name}-lang-pack-pt_br
%{_datadir}/%{name}/%{name}_pt_BR.qm
%endif

#--------------------------------------------------------------------

%if %{build_ru}
%package -n %{name}-lang-pack-ru
Summary:	Russian language pack for psi
Group:		System/Internationalization
Requires:	locales-ru
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-ru
This package adds support for russian to psi.

%files -n %{name}-lang-pack-ru
%{_datadir}/%{name}/%{name}_ru.qm
%endif

#--------------------------------------------------------------------

%if %{build_sl}
%package -n %{name}-lang-pack-sl
Summary:	Slovenian language pack for psi
Group:		System/Internationalization
Requires:	locales-sl
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-sl
This package adds support for slovenian to psi.

%files -n %{name}-lang-pack-sl
%{_datadir}/%{name}/%{name}_sl.qm

%endif

#--------------------------------------------------------------------

%if %{build_sv}
%package -n %{name}-lang-pack-sv
Summary:	Swedish language pack for psi
Group:		System/Internationalization
Requires:	locales-sv
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-sv
This package adds support for swedish to psi.

%files -n %{name}-lang-pack-sv
%{_datadir}/%{name}/%{name}_sv.qm
%endif

#--------------------------------------------------------------------

%if %{build_uk}
%package -n %{name}-lang-pack-uk
Summary:	Ukrainian language pack for psi
Group:		System/Internationalization
Requires:	locales-uk
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-uk
This package adds support for ukrainian to psi.

%files -n %{name}-lang-pack-uk
%{_datadir}/%{name}/%{name}_uk.qm
%endif

#--------------------------------------------------------------------

%if %{build_ur_PK}
%package -n %{name}-lang-pack-ur_PK
Summary:	Urdu language pack for psi
Group:		System/Internationalization
Requires:	locales-ur
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-ur_PK
This package adds support for urdu to psi.

%files -n %{name}-lang-pack-ur_PK
%{_datadir}/%{name}/%{name}_ur_PK.qm
%endif

#--------------------------------------------------------------------

%if %{build_vi}
%package -n %{name}-lang-pack-vi
Summary:	Vietnamese language pack for psi
Group:		System/Internationalization
Requires:	locales-vi
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-vi
This package adds support for vietnamese to psi.

%files -n %{name}-lang-pack-vi
%{_datadir}/%{name}/%{name}_vi.qm
%endif

#--------------------------------------------------------------------

%if %{build_zh_TW}
%package -n %{name}-lang-pack-zh
Summary:	Chinese language pack for psi
Group:		System/Internationalization
Requires:	locales-zh
Provides:	%{name}-lang-pack = %{EVRD}

%description -n %{name}-lang-pack-zh
This package adds support for Chinese to psi.

%files -n %{name}-lang-pack-zh
%{_datadir}/%{name}/%{name}_zh_TW.qm
%{_datadir}/%{name}/%{name}_zh_CN.qm
%endif

#--------------------------------------------------------------------

%prep
%setup -q
%setup -q -T -D -a1 -a2 -a3

%cmake_qt5 -G Ninja

%build
cd build
%ninja_build

%install
%ninja_install -C build

# Install smileysets
cp %{name}-smileysets/* %{buildroot}%{_datadir}/%{name}/iconsets/emoticons
# Install iconsets
cp %{name}-iconsets/* %{buildroot}%{_datadir}/%{name}/iconsets/system

%{expand:%(\
	i=4; \
	for lang in %langlist; do\
		echo "%%{expand:bzip2 -dc %{SOURCE$i} > %{buildroot}/%{_datadir}/%{name}/%{name}_$lang.qm}" ;\
		i=$[i+1];\
	done\
	)
}

# icons
install -D -m 644 %{name}48.png %{buildroot}%{_liconsdir}/%{name}.png
install -D -m 644 %{name}32.png %{buildroot}%{_iconsdir}/%{name}.png
install -D -m 644 %{name}16.png %{buildroot}%{_miconsdir}/%{name}.png
