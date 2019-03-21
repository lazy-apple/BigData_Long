import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

/**
 * @author LaZY(李志一)
 * @create 2019-03-20 13:54
 */
public class LReduce extends Reducer <Text, IntWritable, Text, IntWritable>{
    @Override
    protected void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
            for(IntWritable iw : values){
                context.write(key,new IntWritable(iw.get()));
            }

    }
}
