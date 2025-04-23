# Copyright 2020 Andrii Skrypka
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade

_column_copies = {
    'uom_category': [
        ('measure_type', None, None),
    ],
}

def fix_sequence_column(env):
    """Fix the sequence column type mismatch"""
    env.cr.execute("""
        ALTER TABLE uom_uom
        ALTER COLUMN sequence
        SET DEFAULT 1
    """)

@openupgrade.migrate()
def migrate(env, version):
    fix_sequence_column(env)
    openupgrade.copy_columns(env.cr, _column_copies)
    openupgrade.map_values(
        env.cr,
        openupgrade.get_legacy_name('measure_type'),
        'measure_type',
        [('time', 'working_time')],
        table='uom_category',
    )
