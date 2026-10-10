# Reproducibility

A reproducible FAHIMTA evaluation should preserve enough information for another researcher to understand and repeat the evaluation. Keep software-test reproducibility distinct from reproducing a target model's output.

## Minimum evaluation record

- `evaluation_id`
- `input`
- `expected_behavior`
- `n_atlas_output`
- `evaluation_method`
- `score`
- `error_category`
- `diagnosis`
- `improvement_action`
- `re_evaluation_result`
- `timestamp`
- `version`

## Local software-test procedure

The MVP tests do not require an N-ATLaS model download or paid inference.

1. Obtain the intended repository revision and record its commit SHA. A source ZIP can be used if Git access is unavailable, but record the ZIP's source revision.
2. Use Python 3.11, matching `.github/workflows/tests.yml`.
3. Create and activate a virtual environment.
4. Install the pinned test dependency with `python -m pip install -r requirements-test.txt`.
5. Run `python -m pytest -q` from the repository root.
6. Record the commit/source revision, Python version, pytest version, exact command, complete output, exit status, and any environment limitations.

Example commands:

**Windows PowerShell**
```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-test.txt
python --version
python -m pytest --version
python -m pytest -q
```

**Linux/macOS**
```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-test.txt
python --version
python -m pytest --version
python -m pytest -q
```

The pinned test dependency is recorded in `requirements-test.txt`. The test workflow uses the same file to reduce drift between local and CI runs.

## Environment and model provenance

Record the software version, execution environment, and any external model/system version needed to reproduce the case. For target-model evaluations, also record the actual backend/model ID and revision, generation settings, capture time, and relevant access path when available. If these cannot be verified, state that limitation rather than infer the values.

## Reproducibility rule

Do not claim an evaluation is reproducible unless the input, method, scoring rule, relevant system output, and execution/version context are preserved.

A passing software test suite does not validate Hausa semantic judgements, verify N-ATLaS backend provenance, or prove direct FAHIMTA–N-ATLaS integration.
