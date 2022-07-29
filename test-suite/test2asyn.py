import requests
import statistics
import asyncio
import aiohttp

def get_tasks(session,trials,base_url):
    tasks = []
    for i in range(trials-1):
        tasks.append(session.get(f'{base_url}/app', ssl=False))
    return tasks

async def get_timedata(trials,timedata,base_url):
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session,trials,base_url)
        r4 = await asyncio.gather(*tasks)
        for i in range(trials-1):
            timedata[i] = await (r4[i].elapsed.total_seconds()) * 1000


base_url = "http://localhost:8000"
trials=100
time_data=list(range(trials-1))
time_stats={}

asyncio.run(get_timedata(trials,time_data,base_url))

#number of calls made
time_stats['n']=trials
#median
time_stats['median']=statistics.median(time_data)
#mean
time_stats['mean']=statistics.mean(time_data)
#standard deviation
time_stats['standard deviation']=statistics.pstdev(time_data)
#max
time_stats['max']=max(time_data)
#min
time_stats['min']=min(time_data)
print(time_stats)