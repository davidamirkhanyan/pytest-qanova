import pytest
import asyncio
from Interface.SessionManager import SessionManager
from Interface.TestManager import TestManager
import json

api_token = "eyJraWQiOiJvSVVwNGxoazBjSWUyMHJ4bmdSU0F0U3V3eVVwdVJ0eDZ3QzUzZk9UTHdrPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJhNmZjM2I1OS00OGE4LTQ5MmYtOWRmNS1hMDI2MTAzZTA4Y2IiLCJldmVudF9pZCI6IjY3M2I0ODExLTcyZTQtNGUxMi1hNTlhLTVlNzE2ZmE0YTUwZiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NzA5Mzk0NDksImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy13ZXN0LTIuYW1hem9uYXdzLmNvbVwvdXMtd2VzdC0yXzZkMDZrVnRVbCIsImV4cCI6MTY3MTAxNTc5OSwiaWF0IjoxNjcxMDEyMTk5LCJqdGkiOiI0YzBkMjhjNi04YTA5LTQ0MDMtOTljOC1hODg5NTIzNDQ1NjIiLCJjbGllbnRfaWQiOiJhNXZiazJpbjg1a2JrdWVzY2U0c292NHUyIiwidXNlcm5hbWUiOiJkYXZpdGFtX3N1cGVyYW5ub3RhdGUuY29tIn0.apbHMGpMSUX7fw-xD4JLjeDqwDtER_Kx0C4MwsGZKU68_R5vHdXtHg3VL3I-RapoR_REwtqXzdf1fMPaXZES71Ec2W_hnQNjCbArOkC3nIeQBvSLKKNVuCm2zMYWvjwE8JzMs_XAZOB2Z28sJO8xflCAyovxXAY4qS1C86Vl0z6DsELFa8z5kRKbWeS5e5t7OlDf8jS-ZMETcv-zFYVF6ZTxacejcHcMiOXWOiHJpAUOS3pWDfE8wU61CvMBEX_HhBEac7y-oTrUu8cJ7P7Qu4b3FpCGokqRg0yT7QHbcofXD3jfwxpd01I4TKoxvHaRfZZBJahU5Hi29QDUSZXMqw:eyJraWQiOiJ3V0s1TDhpR0RvaW1MS3hkejVnaXFyTllQVzBvdW1wOEQ4a3ZcLzZVRXZjUT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhNmZjM2I1OS00OGE4LTQ5MmYtOWRmNS1hMDI2MTAzZTA4Y2IiLCJhdWQiOiJhNXZiazJpbjg1a2JrdWVzY2U0c292NHUyIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImV2ZW50X2lkIjoiNjczYjQ4MTEtNzJlNC00ZTEyLWE1OWEtNWU3MTZmYTRhNTBmIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2NzA5Mzk0NDksImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy13ZXN0LTIuYW1hem9uYXdzLmNvbVwvdXMtd2VzdC0yXzZkMDZrVnRVbCIsImNvZ25pdG86dXNlcm5hbWUiOiJkYXZpdGFtX3N1cGVyYW5ub3RhdGUuY29tIiwiZXhwIjoxNjcxMDE1Nzk5LCJpYXQiOjE2NzEwMTIxOTksImVtYWlsIjoiZGF2aXRhbUBzdXBlcmFubm90YXRlLmNvbSJ9.Gt3Y958jFVOST3tUes2QRdkaVEPM6qJsVA92jIKnh_Vm3vFjRiHrJgCH9RbPEPwFm0FaSIq4uMY5cJregXGaCZofDI-IF4nZ_mOHuQ9GZV8nqbUVWRF07cxOIuFybIH6vrfunGdhNh82GCgTrpluyHmJmWPWMGW659Xai_JjW4JT7IEhZhCWIqQrGmngOCf9bKbTO8eBmLplkg0uxDwgTCvbBo4rc6ZrE3JVoNmthUg5iVGdoqQ2DCkn-4RuoQYMnEnt4meQbTHUJvFv_85-f0Jhrz1V8FrnKjPMrRsUCUONLieGj485GP0n26riPa2HJ616hD6IMx-y8aGlz5SeVg"
test_info_dict = {}


def pytest_configure(config):
    """Hook to configure pytest and collect starting variables."""
    command_line = ' '.join(config.invocation_params.args)
    rootdir = str(config.rootdir)
    inifile = str(config.inifile) if config.inifile else None
    args = config.args
    options = {key: value for key, value in vars(config.option).items()}
    # TODO session creation here
    session_id = 1234
    config.session_id = session_id
    config.session_info = {
        'session_id': session_id,
        'state': 1,
        'command_line': command_line,
        'rootdir': rootdir,
        'inifile': inifile,
        'args': args,
        'options': options
        }
    session_manager = SessionManager(api_token)
    config.session_manager = session_manager
    asyncio.run(session_manager.start_session())

        
@pytest.hookimpl(tryfirst=True)
def pytest_configure_node(node):
    """xdist hook"""
    node.workerinput['session_id'] = node.config.session_id


def pytest_collection_modifyitems(config, items):
    for item in items:
        nodeid = item.nodeid
        if hasattr(config, 'workerinput'):
            item.session_id = config.workerinput['session_id']
        else:
            item.session_id = config.session_id
        test_info_dict[nodeid] = {
            'nodeid': nodeid,
            'session_id': item.session_id,
            'name': item.name,
            'path': str(item.fspath),
            'location': item.location,
            'markers': [{marker.name: marker.kwargs if marker.kwargs else None} for marker in item.iter_markers()],
            'status': 'collected',
            'results': {
                'setup': {'outcome': None, 'duration': None},
                'call': {'outcome': None, 'duration': None},
                'teardown': {'outcome': None, 'duration': None},
                }
            }
    with open('test_results.json', 'w') as t:
        json.dump({
            'tests': list(test_info_dict.values()),
            'session_info': config.session_info
            }, t, indent=4)


def pytest_runtest_logreport(report):
    nodeid = report.nodeid
    if nodeid in test_info_dict:
        session_id = test_info_dict[nodeid]['session_id']
        phase = report.when
        if phase == 'setup':
            test_info_dict[nodeid]['status'] = 'in progress'
        test_info_dict[nodeid]['results'][phase]['outcome'] = report.outcome
        test_info_dict[nodeid]['results'][phase]['duration'] = report.duration
        if report.outcome == 'failed':
            error_type, error_message = extract_error_type(report)
            test_info_dict[nodeid]['results'][phase]['longrepr'] = str(report.longrepr) if report.failed else None
            test_info_dict[nodeid]['results'][phase]['error_type'] = error_type
            test_info_dict[nodeid]['results'][phase]['error_message'] = error_message
        if phase == 'teardown':
            test_info_dict[nodeid]['status'] = 'done'
            tm = TestManager(api_token)
            tm.log_test_result(session_id=session_id, result=test_info_dict[nodeid])
            
            # This part is for local testing
            with open('test_results.json', 'r') as t:
                data = json.load(t)
            
            target_result = [item for item in data['tests'] if item['nodeid']==nodeid][0]
            target_index = data['tests'].index(target_result)
            data['tests'][target_index] = test_info_dict[nodeid]
            
            with open('test_results.json', 'w') as t:
                json.dump(data, t)
    
    
def extract_error_type(report):
    if report.failed:
        if hasattr(report.longrepr, 'reprcrash'):
            error_type, error_message = report.longrepr.reprcrash.message.split(': ', 1)
            return error_type, error_message
    else:
        return None, None
    
    
