# poll-the-trump

`select reply_id, 
count(id) as count, 
SUM(case when vote=1 then 1 else 0 end) as pos_votes, 
SUM(case when vote=-1 then 1 else 0 end) as neg_votes ,
sum(abs(vote))/count(id) as polarity_rate
from tweets where reply_id IS NOT NULL 
group by reply_id 
having count > 20 order by reply_id desc`
