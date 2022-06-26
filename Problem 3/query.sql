/* getting current application */
WITH current_application as (
select app.id, 
       app.user_id,
       app.status, 
       max(app.create_timestamp) as create_timestamp, 
       user.mobile_number,
       count(user.mobile_number) as ttl_mobile_count 
from application as app
left join user
on app.user_id=user.id
group by user.mobile_number
),
/* getting past approved application */
past_approved_application as(
select app.id as past_id, 
       app.user_id as past_user_id ,
       max(app.create_timestamp) as past_create_timestamp, 
       user.mobile_number,
       app.status
from application as app
left join user
on app.user_id=user.id
where status="Approved"
group by user.mobile_number
),
/* combining both together to get full dataframe*/
merged_current_approved_app as(
select cur.id,
       cur.user_id,
       cur.status,
       cur.create_timestamp,
       past.past_id,
       past.past_user_id,
       past.past_create_timestamp,
       cur.mobile_number,
       cur.ttl_mobile_count,
       sum(case when past.past_user_id = cur.user_id and past.status="Approved" then 0 else 1 end) as past_approved_ct
from current_application as cur
left join past_approved_application as past
on cur.mobile_number=past.mobile_number)

/* getting final output in required format */
select id, 
       user_id,
       status,
       create_timestamp,
       ("{id: "||past_id||", user_id: "||past_user_id||", create_timestamp: "||past_create_timestamp || "}")as last_approved_application,
       past_approved_ct*1.0/ttl_mobile_count*1.0 as historical_approval_ratio
from merged_current_approved_app;
