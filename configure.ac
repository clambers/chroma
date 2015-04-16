AC_PREREQ([2.69])

AC_INIT([Chroma], [1.0], [https://github.com/PDXostc/chroma/issues], [], [https://github.com/PDXostc/chroma])
AC_CONFIG_SRCDIR([src/index.html])
AC_CONFIG_AUX_DIR([build-aux])

AM_INIT_AUTOMAKE([1.14 foreign -Wall -Werror -Wno-portability])
AM_SILENT_RULES([yes])

AC_CHECK_TOOL([ZIP], [zip])
AC_CHECK_TOOL([XML_LINT], [xmllint])

AC_CONFIG_FILES([Makefile src/Makefile src/chroma.xml])

AC_OUTPUT
