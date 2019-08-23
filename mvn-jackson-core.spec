#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jackson-core
Version  : 2.1.5
Release  : 8
URL      : https://github.com/FasterXML/jackson-core/archive/jackson-core-2.1.5.tar.gz
Source0  : https://github.com/FasterXML/jackson-core/archive/jackson-core-2.1.5.tar.gz
Source1  : https://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.1.5/jackson-core-2.1.5.jar
Source2  : https://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.1.5/jackson-core-2.1.5.pom
Source3  : https://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.6.6/jackson-core-2.6.6.jar
Source4  : https://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.6.6/jackson-core-2.6.6.pom
Source5  : https://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.6.7/jackson-core-2.6.7.jar
Source6  : https://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.6.7/jackson-core-2.6.7.pom
Source7  : https://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.8.6/jackson-core-2.8.6.jar
Source8  : https://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.8.6/jackson-core-2.8.6.pom
Source9  : https://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.9.5/jackson-core-2.9.5.jar
Source10  : https://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.9.5/jackson-core-2.9.5.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-jackson-core-data = %{version}-%{release}

%description
# Overview
This project contains core core low-level incremental ("streaming") parser and generator abstractions used by
[Jackson Data Processor](http://wiki.fasterxml.com/JacksonHome).
It also includes the default implementation of handler types (parser, generator) that handle JSON format.
The core abstractions are not JSON specific, although naming does contain 'JSON' in many places, due to historical reasons. Only packages that specifically contain word 'json' are JSON-specific.

%package data
Summary: data components for the mvn-jackson-core package.
Group: Data

%description data
data components for the mvn-jackson-core package.


%prep
%setup -q -n jackson-core-jackson-core-2.1.5

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.1.5
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.1.5/jackson-core-2.1.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.1.5
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.1.5/jackson-core-2.1.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.6.6
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.6.6/jackson-core-2.6.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.6.6
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.6.6/jackson-core-2.6.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.6.7
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.6.7/jackson-core-2.6.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.6.7
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.6.7/jackson-core-2.6.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.8.6
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.8.6/jackson-core-2.8.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.8.6
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.8.6/jackson-core-2.8.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.9.5
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.9.5/jackson-core-2.9.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.9.5
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.9.5/jackson-core-2.9.5.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.1.5/jackson-core-2.1.5.jar
/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.1.5/jackson-core-2.1.5.pom
/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.6.6/jackson-core-2.6.6.jar
/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.6.6/jackson-core-2.6.6.pom
/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.6.7/jackson-core-2.6.7.jar
/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.6.7/jackson-core-2.6.7.pom
/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.8.6/jackson-core-2.8.6.jar
/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.8.6/jackson-core-2.8.6.pom
/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.9.5/jackson-core-2.9.5.jar
/usr/share/java/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.9.5/jackson-core-2.9.5.pom
