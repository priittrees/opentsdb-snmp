# This file is part of opentsdb-snmp.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.  This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser
# General Public License for more details.  You should have received a copy
# of the GNU Lesser General Public License along with this program.  If not,
# see <http://www.gnu.org/licenses/>.
from nose.tools import eq_, ok_, raises
from opentsdb.snmp.resolvers.nec_paso import NECIPasoModem, NECPasoNEOModem


class TestDevice(object):
    def test_legit_ipaso_resolver(self):
        resolver = NECIPasoModem()

        tags = resolver.resolve("16842752.2")
        eq_("modem1", tags["interface"])
        eq_("es", tags["type"])

        tags = resolver.resolve("16842752.1")
        ok_(not tags)


        tags = resolver.resolve(25231360)
        ok_("type" not in tags)
        eq_("modem2", tags["interface"])

    @raises(Exception)
    def test_missing_ipaso_index(self):
        resolver = NECIPasoModem()
        resolver.resolve(2345)

    def test_pasoneo(self):
        resolver = NECPasoNEOModem()
        tags = resolver.resolve(2)
        eq_("modem2", tags["interface"])
