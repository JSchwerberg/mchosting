# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MinecraftFeature'
        db.create_table(u'hosting_minecraftfeature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('internal_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('short_desc', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('required_memory', self.gf('django.db.models.fields.BigIntegerField')()),
            ('required_storage', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'hosting', ['MinecraftFeature'])

        # Adding model 'MinecraftPlan'
        db.create_table(u'hosting_minecraftplan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('short_desc', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('max_memory', self.gf('django.db.models.fields.BigIntegerField')()),
            ('max_storage', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'hosting', ['MinecraftPlan'])

        # Adding M2M table for field included_features on 'MinecraftPlan'
        m2m_table_name = db.shorten_name(u'hosting_minecraftplan_included_features')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('minecraftplan', models.ForeignKey(orm[u'hosting.minecraftplan'], null=False)),
            ('minecraftfeature', models.ForeignKey(orm[u'hosting.minecraftfeature'], null=False))
        ))
        db.create_unique(m2m_table_name, ['minecraftplan_id', 'minecraftfeature_id'])

        # Adding model 'MinecraftService'
        db.create_table(u'hosting_minecraftservice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('plan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hosting.MinecraftPlan'])),
        ))
        db.send_create_signal(u'hosting', ['MinecraftService'])

        # Adding M2M table for field features on 'MinecraftService'
        m2m_table_name = db.shorten_name(u'hosting_minecraftservice_features')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('minecraftservice', models.ForeignKey(orm[u'hosting.minecraftservice'], null=False)),
            ('minecraftfeature', models.ForeignKey(orm[u'hosting.minecraftfeature'], null=False))
        ))
        db.create_unique(m2m_table_name, ['minecraftservice_id', 'minecraftfeature_id'])


    def backwards(self, orm):
        # Deleting model 'MinecraftFeature'
        db.delete_table(u'hosting_minecraftfeature')

        # Deleting model 'MinecraftPlan'
        db.delete_table(u'hosting_minecraftplan')

        # Removing M2M table for field included_features on 'MinecraftPlan'
        db.delete_table(db.shorten_name(u'hosting_minecraftplan_included_features'))

        # Deleting model 'MinecraftService'
        db.delete_table(u'hosting_minecraftservice')

        # Removing M2M table for field features on 'MinecraftService'
        db.delete_table(db.shorten_name(u'hosting_minecraftservice_features'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hosting.minecraftfeature': {
            'Meta': {'ordering': "['name']", 'object_name': 'MinecraftFeature'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'required_memory': ('django.db.models.fields.BigIntegerField', [], {}),
            'required_storage': ('django.db.models.fields.BigIntegerField', [], {}),
            'short_desc': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        u'hosting.minecraftplan': {
            'Meta': {'ordering': "['name']", 'object_name': 'MinecraftPlan'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'included_features': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['hosting.MinecraftFeature']", 'symmetrical': 'False'}),
            'max_memory': ('django.db.models.fields.BigIntegerField', [], {}),
            'max_storage': ('django.db.models.fields.BigIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'short_desc': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        u'hosting.minecraftservice': {
            'Meta': {'ordering': "['id']", 'object_name': 'MinecraftService'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['hosting.MinecraftFeature']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hosting.MinecraftPlan']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['hosting']