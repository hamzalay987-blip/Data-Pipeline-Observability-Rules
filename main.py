import csv
from datetime import datetime

def run(path='data/manifest.csv',as_of='2026-01-04T12:00:00'):
    now=datetime.fromisoformat(as_of); problems={}; checked=0
    with open(path,newline='') as f:
        for r in csv.DictReader(f):
            checked+=1; reasons=[]
            lag=(now-datetime.fromisoformat(r['last_success'])).total_seconds()/3600
            if lag>float(r['max_age_hours']): reasons.append('stale')
            if float(r['null_rate'])>float(r['max_null_rate']): reasons.append('null_rate')
            if int(r['row_count'])<int(r['min_rows']): reasons.append('low_row_count')
            if reasons: problems[r['dataset']]=reasons
    return {'datasets_checked':checked,'failed_checks':problems}

if __name__ == '__main__':
    import json
    print(json.dumps(run(), indent=2))
