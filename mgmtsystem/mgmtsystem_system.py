# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields, orm


class mgmtsystem_system(orm.Model):

    _name = 'mgmtsystem.system'
    description = 'System'

    _columns = {
<<<<<<< 246504adbebf5957ae9fe262cb1b09aa7213ab41
        'name': fields.char('System', size=30, required=True, translate=True),
        'manual': fields.many2one('wiki.wiki', 'Manual'),
=======
        'name': fields.char('System', size=30, required=True),
        'manual': fields.many2one('document.page', 'Manual'),
>>>>>>> [IMP] Update hooks with addons modules from v7
        'company_id': fields.many2one('res.company', 'Company')
        }

    _defaults = {
        'company_id': lambda self, cr, uid, c: self.pool.get('res.users').browse(cr, uid, uid, c).company_id.id,
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
