
--задание 1
select id_client, sum(sum_tran) as spend_30d from   transact
where  tran_time >= current_date - 30 and  tran_time <  current_date
group by id_client;


--задание 2
with top_clients as (
    select id_client
 from transact
    group by id_client
    order by sum(sum_tran) desc
    limit 100
)
select t.id_client, date_trunc('month', t.tran_time) as month, sum(t.sum_tran) as spend from transact t
join top_clients tc on t.id_client = tc.id_client
group by t.id_client, date_trunc('month', t.tran_time)
order by t.id_client, month;
