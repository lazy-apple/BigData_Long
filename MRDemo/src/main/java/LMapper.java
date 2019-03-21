import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

/**
 * @author LaZY(李志一)
 * @create 2019-03-20 13:54
 */
public class LMapper extends Mapper <LongWritable, Text, Text, IntWritable>{
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        Text keyOut = new Text();
        IntWritable valueOut = new IntWritable();
        String[] arr = value.toString().split(",");
        if (arr.length>1){
            String jsid = arr[0];//'id': 862,
            String jsname = arr[1];//'name': '安康'
            String[] ids = jsid.split(": ");
            int id = Integer.parseInt(ids[1]);//862
            String[] names = jsname.split(": ");
            String name = names[1];//'安康'
            keyOut.set(name);
            valueOut.set(id);
            context.write(keyOut,valueOut);//'安康'：862
        }

    }
}
