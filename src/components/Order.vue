<template>
  <div>
    <h1>Заказы</h1>
    <table>
      <thead>
        <th>Наименование</th>
        <th>Время создания</th>
        <th>Цена</th>
        <th>Доставка</th>
        <th>Общая цена</th>
        <th>Статус</th>
      </thead>
      <tbody>
        <tr v-for="n in ndata" :key=n.Id>
          <td>{{ n.Title | titleFormat }}</td>
          <td>{{ n.DateCreated | dateFormat }}</td>
          <td>{{ n.Price | priceFormat }}</td>
          <td>{{ n.DeliveryPrice | priceFormat }}</td>
          <td>{{ n.TotalPrice | priceFormat }}</td>
          <td>{{ n.PaymentStatus | statusLocale }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import moment from 'moment'

// подключение локального json файла, который получил с python-скрипта
const json = require("../../static/data.json")

export default {
  name: 'Order',
  data () {
    return {
      ndata: json.Result
    }
  },
  filters: { 
    // приведение к более удобочитаемой дате
    dateFormat: date => moment(new Date(parseInt(date.replace("/Date(", "").replace(")/",""), 10))).format('hh:mm, MM.DD.YY'),
    
    // наименования больше 20 знаков обрезаются
    titleFormat: title => title.length > 20 ? (title.slice(0,20) + '...') : title,
    
    // цены учитаны так, что общая сумма не должна достигать миллиона
    priceFormat: price => {
      if (!parseFloat(price)) {return "Отсутствует";}
 
      let p = parseFloat(price).toFixed(2)
 
      if (parseInt(p).toString().length > 3) {
        return p.toString().replace(/\B(?=(\d{3})+\b)/g, ",") + " руб"
      }

      if (p < 1) {
        return parseFloat(price).toFixed(2) + " руб"
      }

      return p + " руб";
    },
    
    // поскольку всего 1 вариант, такая конструкция (но для расширения я бы переписал)
    statusLocale: status => status == 'NotPaid'? 'Не оплачено' : status
  }
}
</script>

<style>
table {
  margin: 10px auto;
  padding: 0 20px;
  border: 1px solid #ccc;
  border-spacing: 0;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  box-shadow: 0px 0px 10px #ccc;
}

td, th {
  padding: 20px 10px;
  border-bottom: 1px solid #ccc;
}

tr:last-child > td {
  border: none;
}

@media (max-width: 1024px) {
  td:nth-child(3), td:nth-child(4), 
  th:nth-child(3), th:nth-child(4) {
    display: none;
  }
}

@media (max-width: 768px) {
  td:nth-child(2), td:last-child, 
  th:nth-child(2), th:last-child {
    display: none;
  }
}
</style>