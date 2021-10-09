#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x24CCD8550E5D1CAE (ban@ban.netlib.re)
#
Name     : geany
Version  : 1.38
Release  : 34
URL      : https://download.geany.org/geany-1.38.tar.gz
Source0  : https://download.geany.org/geany-1.38.tar.gz
Source1  : https://download.geany.org/geany-1.38.tar.gz.sig
Summary  : A fast and lightweight IDE using GTK+
Group    : Development/Tools
License  : GPL-2.0 HPND
Requires: geany-bin = %{version}-%{release}
Requires: geany-data = %{version}-%{release}
Requires: geany-lib = %{version}-%{release}
Requires: geany-license = %{version}-%{release}
Requires: geany-locales = %{version}-%{release}
Requires: geany-man = %{version}-%{release}
BuildRequires : gtk3-dev
BuildRequires : intltool
BuildRequires : lxml

%description
Geany - A fast and lightweight IDE
----------------------------------
About
-----
Geany is a small and lightweight integrated development environment.
It was developed to provide a small and fast IDE, which has only a
few dependencies from other packages. Another goal was to be as independent
as possible from a special Desktop Environment like KDE or GNOME. So it
is using only the GTK+ toolkit and therefore you need only the
GTK+ runtime libraries to run Geany.

%package bin
Summary: bin components for the geany package.
Group: Binaries
Requires: geany-data = %{version}-%{release}
Requires: geany-license = %{version}-%{release}

%description bin
bin components for the geany package.


%package data
Summary: data components for the geany package.
Group: Data

%description data
data components for the geany package.


%package dev
Summary: dev components for the geany package.
Group: Development
Requires: geany-lib = %{version}-%{release}
Requires: geany-bin = %{version}-%{release}
Requires: geany-data = %{version}-%{release}
Provides: geany-devel = %{version}-%{release}
Requires: geany = %{version}-%{release}

%description dev
dev components for the geany package.


%package doc
Summary: doc components for the geany package.
Group: Documentation
Requires: geany-man = %{version}-%{release}

%description doc
doc components for the geany package.


%package lib
Summary: lib components for the geany package.
Group: Libraries
Requires: geany-data = %{version}-%{release}
Requires: geany-license = %{version}-%{release}

%description lib
lib components for the geany package.


%package license
Summary: license components for the geany package.
Group: Default

%description license
license components for the geany package.


%package locales
Summary: locales components for the geany package.
Group: Default

%description locales
locales components for the geany package.


%package man
Summary: man components for the geany package.
Group: Default

%description man
man components for the geany package.


%prep
%setup -q -n geany-1.38
cd %{_builddir}/geany-1.38

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633819386
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --enable-gtk3 \
--disable-api-docs
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1633819386
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/geany
cp %{_builddir}/geany-1.38/COPYING %{buildroot}/usr/share/package-licenses/geany/1bba544d91de647b97f45a31e63540d6d5d06096
cp %{_builddir}/geany-1.38/scintilla/License.txt %{buildroot}/usr/share/package-licenses/geany/f06de8b018290a99ff91fa2f136ad3b859ae8543
%make_install
%find_lang geany

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/geany

%files data
%defattr(-,root,root,-)
/usr/share/applications/geany.desktop
/usr/share/geany/GPL-2
/usr/share/geany/colorschemes/alt.conf
/usr/share/geany/filedefs/filetypes.Arduino.conf
/usr/share/geany/filedefs/filetypes.CUDA.conf
/usr/share/geany/filedefs/filetypes.Clojure.conf
/usr/share/geany/filedefs/filetypes.Cython.conf
/usr/share/geany/filedefs/filetypes.Genie.conf
/usr/share/geany/filedefs/filetypes.Graphviz.conf
/usr/share/geany/filedefs/filetypes.Groovy.conf
/usr/share/geany/filedefs/filetypes.JSON.conf
/usr/share/geany/filedefs/filetypes.Kotlin.conf
/usr/share/geany/filedefs/filetypes.Meson.conf
/usr/share/geany/filedefs/filetypes.Nim.conf
/usr/share/geany/filedefs/filetypes.Scala.conf
/usr/share/geany/filedefs/filetypes.Swift.conf
/usr/share/geany/filedefs/filetypes.TypeScript.conf
/usr/share/geany/filedefs/filetypes.abaqus
/usr/share/geany/filedefs/filetypes.abc
/usr/share/geany/filedefs/filetypes.actionscript
/usr/share/geany/filedefs/filetypes.ada
/usr/share/geany/filedefs/filetypes.asciidoc
/usr/share/geany/filedefs/filetypes.asm
/usr/share/geany/filedefs/filetypes.batch
/usr/share/geany/filedefs/filetypes.bibtex
/usr/share/geany/filedefs/filetypes.c
/usr/share/geany/filedefs/filetypes.caml
/usr/share/geany/filedefs/filetypes.cmake
/usr/share/geany/filedefs/filetypes.cobol
/usr/share/geany/filedefs/filetypes.coffeescript
/usr/share/geany/filedefs/filetypes.common
/usr/share/geany/filedefs/filetypes.conf
/usr/share/geany/filedefs/filetypes.cpp
/usr/share/geany/filedefs/filetypes.cs
/usr/share/geany/filedefs/filetypes.css
/usr/share/geany/filedefs/filetypes.d
/usr/share/geany/filedefs/filetypes.diff
/usr/share/geany/filedefs/filetypes.docbook
/usr/share/geany/filedefs/filetypes.erlang
/usr/share/geany/filedefs/filetypes.f77
/usr/share/geany/filedefs/filetypes.ferite
/usr/share/geany/filedefs/filetypes.forth
/usr/share/geany/filedefs/filetypes.fortran
/usr/share/geany/filedefs/filetypes.freebasic
/usr/share/geany/filedefs/filetypes.glsl
/usr/share/geany/filedefs/filetypes.go
/usr/share/geany/filedefs/filetypes.haskell
/usr/share/geany/filedefs/filetypes.haxe
/usr/share/geany/filedefs/filetypes.html
/usr/share/geany/filedefs/filetypes.java
/usr/share/geany/filedefs/filetypes.javascript
/usr/share/geany/filedefs/filetypes.julia
/usr/share/geany/filedefs/filetypes.latex
/usr/share/geany/filedefs/filetypes.lisp
/usr/share/geany/filedefs/filetypes.lua
/usr/share/geany/filedefs/filetypes.makefile
/usr/share/geany/filedefs/filetypes.markdown
/usr/share/geany/filedefs/filetypes.matlab
/usr/share/geany/filedefs/filetypes.nsis
/usr/share/geany/filedefs/filetypes.objectivec
/usr/share/geany/filedefs/filetypes.pascal
/usr/share/geany/filedefs/filetypes.perl
/usr/share/geany/filedefs/filetypes.php
/usr/share/geany/filedefs/filetypes.po
/usr/share/geany/filedefs/filetypes.powershell
/usr/share/geany/filedefs/filetypes.python
/usr/share/geany/filedefs/filetypes.r
/usr/share/geany/filedefs/filetypes.restructuredtext
/usr/share/geany/filedefs/filetypes.ruby
/usr/share/geany/filedefs/filetypes.rust
/usr/share/geany/filedefs/filetypes.sh
/usr/share/geany/filedefs/filetypes.smalltalk
/usr/share/geany/filedefs/filetypes.sql
/usr/share/geany/filedefs/filetypes.tcl
/usr/share/geany/filedefs/filetypes.txt2tags
/usr/share/geany/filedefs/filetypes.vala
/usr/share/geany/filedefs/filetypes.verilog
/usr/share/geany/filedefs/filetypes.vhdl
/usr/share/geany/filedefs/filetypes.xml
/usr/share/geany/filedefs/filetypes.yaml
/usr/share/geany/filedefs/filetypes.zephir
/usr/share/geany/filetype_extensions.conf
/usr/share/geany/geany-3.0.css
/usr/share/geany/geany-3.20.css
/usr/share/geany/geany.css
/usr/share/geany/geany.glade
/usr/share/geany/snippets.conf
/usr/share/geany/tags/entities.html.tags
/usr/share/geany/tags/std.pas.tags
/usr/share/geany/tags/std.php.tags
/usr/share/geany/tags/std.py.tags
/usr/share/geany/tags/std99.c.tags
/usr/share/geany/templates/bsd
/usr/share/geany/templates/changelog
/usr/share/geany/templates/fileheader
/usr/share/geany/templates/files/file.html
/usr/share/geany/templates/files/file.php
/usr/share/geany/templates/files/file.rb
/usr/share/geany/templates/files/file.tex
/usr/share/geany/templates/files/file_html5.html
/usr/share/geany/templates/files/main.c
/usr/share/geany/templates/files/main.cxx
/usr/share/geany/templates/files/main.d
/usr/share/geany/templates/files/main.java
/usr/share/geany/templates/files/main.py
/usr/share/geany/templates/files/main.vala
/usr/share/geany/templates/files/module.erl
/usr/share/geany/templates/files/program.pas
/usr/share/geany/templates/function
/usr/share/geany/templates/gpl
/usr/share/geany/ui_toolbar.xml
/usr/share/icons/Tango/16x16/actions/geany-save-all.png
/usr/share/icons/Tango/24x24/actions/geany-save-all.png
/usr/share/icons/Tango/32x32/actions/geany-save-all.png
/usr/share/icons/Tango/48x48/actions/geany-save-all.png
/usr/share/icons/Tango/scalable/actions/geany-save-all.svg
/usr/share/icons/hicolor/16x16/actions/geany-build.png
/usr/share/icons/hicolor/16x16/actions/geany-close-all.png
/usr/share/icons/hicolor/16x16/actions/geany-save-all.png
/usr/share/icons/hicolor/16x16/apps/classviewer-class.png
/usr/share/icons/hicolor/16x16/apps/classviewer-macro.png
/usr/share/icons/hicolor/16x16/apps/classviewer-member.png
/usr/share/icons/hicolor/16x16/apps/classviewer-method.png
/usr/share/icons/hicolor/16x16/apps/classviewer-namespace.png
/usr/share/icons/hicolor/16x16/apps/classviewer-other.png
/usr/share/icons/hicolor/16x16/apps/classviewer-struct.png
/usr/share/icons/hicolor/16x16/apps/classviewer-var.png
/usr/share/icons/hicolor/16x16/apps/geany.png
/usr/share/icons/hicolor/24x24/actions/geany-build.png
/usr/share/icons/hicolor/24x24/actions/geany-close-all.png
/usr/share/icons/hicolor/24x24/actions/geany-save-all.png
/usr/share/icons/hicolor/32x32/actions/geany-build.png
/usr/share/icons/hicolor/32x32/actions/geany-close-all.png
/usr/share/icons/hicolor/32x32/actions/geany-save-all.png
/usr/share/icons/hicolor/32x32/apps/geany.png
/usr/share/icons/hicolor/48x48/actions/geany-build.png
/usr/share/icons/hicolor/48x48/actions/geany-close-all.png
/usr/share/icons/hicolor/48x48/actions/geany-save-all.png
/usr/share/icons/hicolor/48x48/apps/geany.png
/usr/share/icons/hicolor/scalable/actions/geany-build.svg
/usr/share/icons/hicolor/scalable/actions/geany-close-all.svg
/usr/share/icons/hicolor/scalable/actions/geany-save-all.svg
/usr/share/icons/hicolor/scalable/apps/geany.svg

%files dev
%defattr(-,root,root,-)
/usr/include/geany/app.h
/usr/include/geany/build.h
/usr/include/geany/dialogs.h
/usr/include/geany/document.h
/usr/include/geany/editor.h
/usr/include/geany/encodings.h
/usr/include/geany/filetypes.h
/usr/include/geany/geany.h
/usr/include/geany/geanyfunctions.h
/usr/include/geany/geanyplugin.h
/usr/include/geany/gtkcompat.h
/usr/include/geany/highlighting.h
/usr/include/geany/keybindings.h
/usr/include/geany/main.h
/usr/include/geany/msgwindow.h
/usr/include/geany/navqueue.h
/usr/include/geany/plugindata.h
/usr/include/geany/pluginutils.h
/usr/include/geany/prefs.h
/usr/include/geany/project.h
/usr/include/geany/scintilla/Compat.h
/usr/include/geany/scintilla/SciLexer.h
/usr/include/geany/scintilla/Sci_Position.h
/usr/include/geany/scintilla/Scintilla.h
/usr/include/geany/scintilla/Scintilla.iface
/usr/include/geany/scintilla/ScintillaWidget.h
/usr/include/geany/sciwrappers.h
/usr/include/geany/search.h
/usr/include/geany/spawn.h
/usr/include/geany/stash.h
/usr/include/geany/support.h
/usr/include/geany/symbols.h
/usr/include/geany/tagmanager/tm_parser.h
/usr/include/geany/tagmanager/tm_source_file.h
/usr/include/geany/tagmanager/tm_tag.h
/usr/include/geany/tagmanager/tm_workspace.h
/usr/include/geany/templates.h
/usr/include/geany/toolbar.h
/usr/include/geany/ui_utils.h
/usr/include/geany/utils.h
/usr/lib64/libgeany.so
/usr/lib64/pkgconfig/geany.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/geany/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/geany/classbuilder.so
/usr/lib64/geany/export.so
/usr/lib64/geany/filebrowser.so
/usr/lib64/geany/htmlchars.so
/usr/lib64/geany/saveactions.so
/usr/lib64/geany/splitwindow.so
/usr/lib64/libgeany.so.0
/usr/lib64/libgeany.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/geany/1bba544d91de647b97f45a31e63540d6d5d06096
/usr/share/package-licenses/geany/f06de8b018290a99ff91fa2f136ad3b859ae8543

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/geany.1

%files locales -f geany.lang
%defattr(-,root,root,-)

