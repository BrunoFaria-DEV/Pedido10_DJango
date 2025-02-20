# Generated by Django 3.2.6 on 2025-02-20 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=50)),
                ('Endereco', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='FormaPGTO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Desc_Forma_PGTO', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome_Produto', models.CharField(max_length=50)),
                ('Descricao', models.CharField(max_length=150)),
                ('Preco', models.DecimalField(decimal_places=2, max_digits=9)),
                ('Imagem', models.ImageField(blank=True, null=True, upload_to='produtos/')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VLR_Total_Pedido', models.DecimalField(decimal_places=2, max_digits=9)),
                ('Pago', models.CharField(max_length=10)),
                ('Status_Pedido', models.CharField(max_length=10)),
                ('DT_Pedido', models.DateField()),
                ('ID_Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cliente')),
                ('ID_FormaPGTO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.formapgto')),
                ('ID_Produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.produto')),
            ],
        ),
    ]
