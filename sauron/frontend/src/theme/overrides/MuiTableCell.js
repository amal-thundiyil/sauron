import palette from '../palette';
import typography from '../typography';

const tableCell = {
  root: {
    ...typography.body1,
    borderBottom: `1px solid ${palette.divider}`,
  },
};

export default tableCell;