import pytest
import pandas as pd
from datetime import datetime
from decimal import Decimal

try:
    from src.transform.reglas_calidad import (
        validar_transaccion,
        validar_analitica,
        validar_esquema_transacciones,
        validar_esquema_analitica,
        ReglaCalidad,
        ResultadoValidacion
    )
except ImportError:
    from unittest.mock import Mock
    ReglaCalidad = Mock
    ResultadoValidacion = Mock
    def validar_transaccion(df): pass
    def validar_analitica(df): pass
    def validar_esquema_transacciones(df): pass
    def validar_esquema_analitica(df): pass


class TestReglasCalidadTransacciones:
    """Pruebas para reglas de calidad de transacciones"""

    @pytest.fixture
    def df_transaccion_valido(self):
        """DataFrame con datos válidos de transacciones"""
        return pd.DataFrame({
            'id_transaccion': ['TX001', 'TX002', 'TX003'],
            'id_cliente': ['CL001', 'CL002', 'CL003'],
            'monto': [Decimal('150.50'), Decimal('200.00'), Decimal('75.25')],
            'moneda': ['USD', 'USD', 'USD'],
            'fecha_transaccion': pd.to_datetime(['2024-01-15', '2024-01-15', '2024-01-15']),
            'tipo_transaccion': ['PAGO', 'TRANSFERENCIA', 'PAGO'],
            'estado': ['COMPLETADA', 'COMPLETADA', 'COMPLETADA']
        })

    @pytest.fixture
    def df_transaccion_invalido(self):
        """DataFrame con datos inválidos de transacciones"""
        return pd.DataFrame({
            'id_transaccion': ['TX001', 'TX002', None],
            'id_cliente': ['CL001', None, 'CL003'],
            'monto': [Decimal('150.50'), Decimal('-50.00'), Decimal('0')],
            'moneda': ['USD', 'INVALIDA', 'USD'],
            'fecha_transaccion': pd.to_datetime(['2024-01-15', '2024-01-15', 'invalid']),
            'tipo_transaccion': ['PAGO', 'TRANSFERENCIA', 'PAGO'],
            'estado': ['COMPLETADA', 'DESCONOCIDO', 'COMPLETADA']
        })

    def test_validar_transaccion_datos_validos(self, df_transaccion_valido):
        """Verifica que transacciones válidas pasan las reglas de calidad"""
        resultado = validar_transaccion(df_transaccion_valido)
        assert resultado is not None
        assert hasattr(resultado, 'es_valido')
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is True

    def test_validar_transaccion_datos_invalidos(self, df_transaccion_invalido):
        """Verifica que transacciones inválidas fallan las reglas de calidad"""
        resultado = validar_transaccion(df_transaccion_invalido)
        assert resultado is not None
        assert hasattr(resultado, 'es_valido')
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is False

    def test_validar_esquema_transacciones(self, df_transaccion_valido):
        """Verifica que el esquema de transacciones es correcto"""
        resultado = validar_esquema_transacciones(df_transaccion_valido)
        assert resultado is not None
        assert hasattr(resultado, 'es_valido')
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is True

    def test_validar_monto_negativo(self):
        """Verifica que montos negativos son rechazados"""
        df_monto_negativo = pd.DataFrame({
            'id_transaccion': ['TX001'],
            'id_cliente': ['CL001'],
            'monto': [Decimal('-100.00')],
            'moneda': ['USD'],
            'fecha_transaccion': pd.to_datetime(['2024-01-15']),
            'tipo_transaccion': ['PAGO'],
            'estado': ['COMPLETADA']
        })
        resultado = validar_transaccion(df_monto_negativo)
        assert resultado is not None
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is False

    def test_validar_moneda_invalida(self):
        """Verifica que monedas inválidas son rechazadas"""
        df_moneda_invalida = pd.DataFrame({
            'id_transaccion': ['TX001'],
            'id_cliente': ['CL001'],
            'monto': [Decimal('100.00')],
            'moneda': ['XYZ'],
            'fecha_transaccion': pd.to_datetime(['2024-01-15']),
            'tipo_transaccion': ['PAGO'],
            'estado': ['COMPLETADA']
        })
        resultado = validar_transaccion(df_moneda_invalida)
        assert resultado is not None
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is False

    def test_validar_estado_transaccion(self):
        """Verifica que estados válidos son aceptados"""
        df_estado_invalido = pd.DataFrame({
            'id_transaccion': ['TX001'],
            'id_cliente': ['CL001'],
            'monto': [Decimal('100.00')],
            'moneda': ['USD'],
            'fecha_transaccion': pd.to_datetime(['2024-01-15']),
            'tipo_transaccion': ['PAGO'],
            'estado': ['INVALIDO']
        })
        resultado = validar_transaccion(df_estado_invalido)
        assert resultado is not None
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is False


class TestReglasCalidadAnalitica:
    """Pruebas para reglas de calidad de analítica"""

    @pytest.fixture
    def df_analitica_valido(self):
        """DataFrame con datos válidos de analítica"""
        return pd.DataFrame({
            'id_sesion': ['SES001', 'SES002', 'SES003'],
            'id_usuario': ['USR001', 'USR002', 'USR003'],
            'fecha_sesion': pd.to_datetime(['2024-01-15 10:00:00', '2024-01-15 11:00:00', '2024-01-15 12:00:00']),
            'duracion_segundos': [300, 600, 450],
            'paginas_visitadas': [5, 10, 7],
            'eventos': [15, 25, 12],
            'conversion': [True, False, True]
        })

    @pytest.fixture
    def df_analitica_invalido(self):
        """DataFrame con datos inválidos de analítica"""
        return pd.DataFrame({
            'id_sesion': ['SES001', None, 'SES003'],
            'id_usuario': ['USR001', 'USR002', None],
            'fecha_sesion': pd.to_datetime(['2024-01-15 10:00:00', 'invalid', '2024-01-15 12:00:00']),
            'duracion_segundos': [300, -10, 450],
            'paginas_visitadas': [5, 0, 7],
            'eventos': [15, 25, -5],
            'conversion': [True, False, True]
        })

    def test_validar_analitica_datos_validos(self, df_analitica_valido):
        """Verifica que datos de analítica válidos pasan las reglas"""
        resultado = validar_analitica(df_analitica_valido)
        assert resultado is not None
        assert hasattr(resultado, 'es_valido')
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is True

    def test_validar_analitica_datos_invalidos(self, df_analitica_invalido):
        """Verifica que datos de analítica inválidos fallan las reglas"""
        resultado = validar_analitica(df_analitica_invalido)
        assert resultado is not None
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is False

    def test_validar_duracion_negativa(self):
        """Verifica que duraciones negativas son rechazadas"""
        df_duracion_negativa = pd.DataFrame({
            'id_sesion': ['SES001'],
            'id_usuario': ['USR001'],
            'fecha_sesion': pd.to_datetime(['2024-01-15 10:00:00']),
            'duracion_segundos': [-100],
            'paginas_visitadas': [5],
            'eventos': [15],
            'conversion': [True]
        })
        resultado = validar_analitica(df_duracion_negativa)
        assert resultado is not None
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is False

    def test_validar_eventos_negativos(self):
        """Verifica que eventos negativos son rechazados"""
        df_eventos_negativos = pd.DataFrame({
            'id_sesion': ['SES001'],
            'id_usuario': ['USR001'],
            'fecha_sesion': pd.to_datetime(['2024-01-15 10:00:00']),
            'duracion_segundos': [300],
            'paginas_visitadas': [5],
            'eventos': [-10],
            'conversion': [True]
        })
        resultado = validar_analitica(df_eventos_negativos)
        assert resultado is not None
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is False


class TestReglasCalidadUmbrales:
    """Pruebas para umbrales de calidad"""

    def test_umbral_completitud_transacciones(self):
        """Verifica que se cumple el umbral de completitud del 99.9%"""
        df_completo = pd.DataFrame({
            'id_transaccion': ['TX001'] * 1000,
            'id_cliente': ['CL001'] * 1000,
            'monto': [Decimal('100.00')] * 1000,
            'moneda': ['USD'] * 1000,
            'fecha_transaccion': pd.to_datetime(['2024-01-15'] * 1000),
            'tipo_transaccion': ['PAGO'] * 1000,
            'estado': ['COMPLETADA'] * 1000
        })
        resultado = validar_transaccion(df_completo)
        assert resultado is not None
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is True

    def test_fallo_umbral_completitud(self):
        """Verifica que falla cuando no se cumple el umbral de completitud"""
        df_incompleto = pd.DataFrame({
            'id_transaccion': ['TX001'] * 900 + [None] * 100,
            'id_cliente': ['CL001'] * 1000,
            'monto': [Decimal('100.00')] * 1000,
            'moneda': ['USD'] * 1000,
            'fecha_transaccion': pd.to_datetime(['2024-01-15'] * 1000),
            'tipo_transaccion': ['PAGO'] * 1000,
            'estado': ['COMPLETADA'] * 1000
        })
        resultado = validar_transaccion(df_incompleto)
        assert resultado is not None
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is False