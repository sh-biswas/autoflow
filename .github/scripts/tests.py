from click.testing import CliRunner
from ../../autoflow.main import new, hello

def test_new():
    runner = CliRunner()
    result = runner.invoke('new')
    assert result.exit_code == 0
    assert result.output == '🔥 creates new project'

def test_hello():
    runner = CliRunner()
    result = runner.invoke('hello')
    assert result.exit_code == 0
    assert result.output == 'Hello'